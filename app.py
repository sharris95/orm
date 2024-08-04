from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Gory1234!@localhost/fitness_center_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    join_date = db.Column(db.Date, nullable=False)

# Define WorkoutSession model
class WorkoutSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    session_date = db.Column(db.Date, nullable=False)
    workout_type = db.Column(db.String(100), nullable=False)
    member = db.relationship('Member', backref='workouts')

# Define Marshmallow schemas for serialization
class MemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Member

class WorkoutSessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutSession

# Initialize schemas
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
workout_session_schema = WorkoutSessionSchema()
workout_sessions_schema = WorkoutSessionSchema(many=True)

# CRUD Operations for Members
@app.route('/members', methods=['POST'])
def add_member():
    try:
        name = request.json['name']
        email = request.json['email']
        join_date = request.json['join_date']
        new_member = Member(name=name, email=email, join_date=join_date)
        db.session.add(new_member)
        db.session.commit()
        return member_schema.jsonify(new_member), 201  # Created status
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400  # Bad Request

@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return members_schema.jsonify(members)

@app.route('/members/<id>', methods=['GET'])
def get_member(id):
    member = Member.query.get(id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    return member_schema.jsonify(member)

@app.route('/members/<id>', methods=['PUT'])
def update_member(id):
    member = Member.query.get(id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    try:
        member.name = request.json['name']
        member.email = request.json['email']
        db.session.commit()
        return member_schema.jsonify(member)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400  # Bad Request

@app.route('/members/<id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get(id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    try:
        db.session.delete(member)
        db.session.commit()
        return jsonify({"message": "Member deleted"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400  # Bad Request

# CRUD Operations for WorkoutSessions
@app.route('/workouts', methods=['POST'])
def add_workout():
    try:
        member_id = request.json['member_id']
        session_date = request.json['session_date']
        workout_type = request.json['workout_type']
        new_workout = WorkoutSession(member_id=member_id, session_date=session_date, workout_type=workout_type)
        db.session.add(new_workout)
        db.session.commit()
        return workout_session_schema.jsonify(new_workout), 201  # Created status
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400  # Bad Request

@app.route('/workouts/<member_id>', methods=['GET'])
def get_workouts_for_member(member_id):
    workouts = WorkoutSession.query.filter_by(member_id=member_id).all()
    return workout_sessions_schema.jsonify(workouts)

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created within application context
    app.run(debug=True, port=5001)  # Start on port 5001

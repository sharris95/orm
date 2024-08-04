Flask-SQLAlchemy Fitness Center Project
Welcome to my Flask-SQLAlchemy Fitness Center Project! This project is a simple web application that allows you to manage a fitness center's database using Flask and SQLAlchemy. I built this project as part of my coding bootcamp assignment for the Introduction to Object-relational Mappers (ORM) course.

Project Overview
This application includes:

Members: Manage fitness center members, including adding, updating, retrieving, and deleting member records.
Workout Sessions: Schedule and view workout sessions for each member.
Technologies Used
Flask: A micro web framework for Python.
Flask-SQLAlchemy: SQLAlchemy integration for Flask.
Flask-Marshmallow: Object serialization/deserialization and validation.
MySQL: Database to store the fitness center data.
Setup Instructions
Clone the Repository:



git clone https://github.com/yourusername/flask_sqlalchemy_fitness_center.git
cd flask_sqlalchemy_fitness_center
Create a Virtual Environment (Recommended):



python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

Make sure you have pip installed, then run:



pip install Flask Flask-SQLAlchemy Flask-Marshmallow mysql-connector-python
Configure Database:

Update the SQLALCHEMY_DATABASE_URI in app.py with your database credentials:

python

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'
Create the Database:

Ensure that the MySQL server is running and the database fitness_center_db is created.

Run the Application:



python app.py
The app will start on http://127.0.0.1:5001.

API Endpoints
Members
Add Member (POST /members):

Request Body: { "name": "John Doe", "email": "john@example.com", "join_date": "2024-08-03" }
Response: JSON representation of the newly added member.
Get All Members (GET /members):

Response: JSON list of all members.
Get Member by ID (GET /members/<id>):

Response: JSON representation of the member with the given ID.
Update Member (PUT /members/<id>):

Request Body: { "name": "John Doe", "email": "john@example.com" }
Response: JSON representation of the updated member.
Delete Member (DELETE /members/<id>):

Response: Confirmation message.
Workout Sessions
Add Workout Session (POST /workouts):

Request Body: { "member_id": 1, "session_date": "2024-08-03", "workout_type": "Yoga" }
Response: JSON representation of the newly added workout session.
Get Workouts for Member (GET /workouts/<member_id>):

Response: JSON list of workout sessions for the specified member.
Guidelines and Notes
Assignment Guidelines: This project is part of the Module 6 Lesson 3 assignment. It transitions from a traditional SQL approach to using Flask-SQLAlchemy for managing a fitness center's database.
Error Handling: Basic error handling is implemented for CRUD operations to manage database errors.
Testing: Use Postman or similar tools to test the API endpoints.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to my coding bootcamp instructors for their guidance.
Thanks to the open-source community for the libraries used.

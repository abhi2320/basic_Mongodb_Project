User Management API with FastAPI and MongoDB

This project implements a set of APIs for user management using FastAPI and MongoDB. The API includes user registration, login, linking IDs, joining data from multiple collections, and chain deleting user data.
I have done APIs testing in POSTMAN.


Requirements
Framework and Libraries
FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
PyMongo: A Python driver for MongoDB to interact with MongoDB databases.

Dependencies
fastapi: FastAPI web framework.
pymongo: MongoDB driver for Python.
bcrypt: Library to hash passwords securely.
pydantic: Data validation and settings management using Python type annotations.
uvicorn: ASGI server to run FastAPI applications.
python-dotenv: Library to manage environment variables.


Setup

Installation
Create a Virtual Environment
python -m venv venv
Activate the Virtual Environment
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

Install Dependencies

pip install fastapi pymongo bcrypt pydantic uvicorn python-dotenv


API Endpoints
Registration API
Endpoint: /register
Method: POST
Description: Register a new user.
Request Body:
{
  "username": "string",
  "email": "string",
  "password": "string"
}
Response:
{
  "message": "User registered successfully."
}


Login API
Endpoint: /login
Method: POST
Description: Authenticate an existing user.
Request Body:
{
  "email": "string",
  "password": "string"
}
Response:
{
  "message": "Login successful."
}


Linking ID API
Endpoint: /link-id
Method: POST
Description: Link an ID to a user's account.
Request Body:
{
  "user_id": "string",
  "id_to_link": "string"
}
Response:
{
  "message": "ID linked successfully."
}

Joins
Endpoint: /join-data
Method: GET
Description: Join data from multiple collections.
Query Parameters:
collection1_id=string
collection2_id=string
Response:
{
  "data": "Joined data from multiple collections."
}

Chain Delete
Endpoint: /delete-user
Method: DELETE
Description: Delete a user and all associated data.
Request Body:
{
  "user_id": "string"
}
Response:
{
  "message": "User and associated data deleted successfully."
}
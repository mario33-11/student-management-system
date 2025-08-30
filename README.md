# Student Management System

A Flask web application for managing student information.

## Features

- Add, edit, delete students
- Search students by ID or name
- View student details
- Clean, responsive UI

## Setup

1. Create virtual environment: `python -m venv venv`
2. Activate: `venv\Scripts\activate`
3. Install requirements: `pip install -r requirements.txt`
4. Initialize database: `flask db init && flask db migrate && flask db upgrade`
5. Run: `python app.py`

## Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-Migrate
- **Frontend**: HTML, CSS (Bootstrap), Jinja2
- **Database**: SQLite

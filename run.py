#!/usr/bin/env python3
"""
Entry point for the Student Management System Flask application.
This file is used to run the application in production or development.
"""

from app import app

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True, host='127.0.0.1', port=5000)

#!/usr/bin/env python3
"""
Database setup script for Student Management System.
Run this script to initialize the database and create tables.
"""

from app import app
from models import db
import click

def setup_database():
    """Initialize the database and create all tables"""
    with app.app_context():
        try:
            # Create all database tables
            db.create_all()
            print("✅ Database tables created successfully!")
            print("✅ Student Management System is ready to use!")
            print("\nTo run the application:")
            print("  python app.py")
            print("  or")
            print("  python run.py")
            print("\nThen visit: http://127.0.0.1:5000")
            
        except Exception as e:
            print(f"❌ Error creating database: {e}")
            return False
    return True

if __name__ == '__main__':
    print("🚀 Setting up Student Management System Database...")
    print("=" * 50)
    setup_database()

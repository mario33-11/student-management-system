from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Student(db.Model):
    """Student model representing the students table"""
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False, default=date.today)
    
    def __repr__(self):
        return f'<Student {self.full_name}>'
    
    def to_dict(self):
        """Convert student object to dictionary"""
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'department': self.department,
            'enrollment_date': self.enrollment_date.strftime('%b %d, %Y')
        }

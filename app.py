from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from models import db, Student
from forms import StudentForm, SearchForm
from config import Config
from datetime import datetime
import click

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    return app

app = create_app()

# Automatically create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    """Display all students in a table"""
    search_form = SearchForm()
    students = Student.query.all()
    return render_template('index.html', students=students, search_form=search_form)

@app.route('/search', methods=['POST'])
def search():
    """Search students by ID, Name or Email"""
    form = SearchForm()
    students = []
    
    if form.validate_on_submit():
        search_query = form.search_query.data.strip()
        
        try:
            student_id = int(search_query)
            students = Student.query.filter_by(id=student_id).all()
        except ValueError:
            students = Student.query.filter(
                db.or_(
                    Student.full_name.contains(search_query),
                    Student.email.contains(search_query)
                )
            ).all()
    
    return render_template('index.html', students=students, search_form=form, search_performed=True)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """Add new student"""
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            full_name=form.full_name.data,
            email=form.email.data,
            phone=form.phone.data,
            department=form.department.data,
            enrollment_date=form.enrollment_date.data
        )
        try:
            db.session.add(student)
            db.session.commit()
            flash('Student added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error: Email already exists!', 'error')
    
    return render_template('add_student.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    """Edit existing student"""
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    
    if form.validate_on_submit():
        try:
            form.populate_obj(student)
            db.session.commit()
            flash('Student updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error: Email already exists!', 'error')
    
    return render_template('edit_student.html', form=form, student=student)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    """Delete student"""
    student = Student.query.get_or_404(id)
    try:
        db.session.delete(student)
        db.session.commit()
        flash('Student deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting student!', 'error')
    
    return redirect(url_for('index'))

@app.route('/details/<int:id>')
def details(id):
    """View single student details"""
    student = Student.query.get_or_404(id)
    return render_template('details.html', student=student)

# CLI Commands for development
@app.cli.command()
def create_tables():
    """Create database tables"""
    db.create_all()
    click.echo('Database tables created!')

if __name__ == '__main__':
    app.run(debug=True)

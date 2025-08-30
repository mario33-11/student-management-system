# Student Management System

A Flask web application for managing student information with a clean, modern UI matching Figma design.

## Features

✨ **Complete CRUD Operations**
- ➕ Add new students with form validation
- 📝 Edit existing student information  
- 🗑️ Delete students with confirmation
- 👁️ View detailed student information

🔍 **Advanced Search**
- Search by Student ID (numeric)
- Search by Student Name (partial match)
- Search by Email address
- Real-time search results

🎨 **Modern UI/UX**
- Responsive design for all devices
- Clean table layout matching Figma mockup
- Bootstrap-powered interface
- Custom CSS styling
- Flash messaging for user feedback

## Quick Start

### 1️⃣ Setup Environment
```bash
# Clone/download the project
# Navigate to project directory
cd student-management-system

# Create virtual environment  
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Database
```bash
python setup.py
```

### 4️⃣ Run Application
```bash
python app.py
# or
python run.py
```

### 5️⃣ Access Application
Open your browser and visit: **http://127.0.0.1:5000**

## Project Structure

```
student-management-system/
├── app.py                 # Main Flask application
├── run.py                 # Alternative entry point
├── setup.py               # Database setup script
├── config.py              # Application configuration
├── models.py              # Database models (Student)
├── forms.py               # WTForms for validation
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore            # Git ignore rules
├── templates/             # Jinja2 HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Student list & search
│   ├── add_student.html  # Add new student form
│   ├── edit_student.html # Edit student form
│   └── details.html      # Student details view
└── static/               # Static assets
    └── css/
        └── style.css     # Custom CSS styling
```

## Database Schema

### Students Table
| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Primary Key (Auto-increment) |
| `full_name` | String(100) | Student full name |
| `email` | String(120) | Email address (unique) |
| `phone` | String(20) | Phone number |
| `department` | String(50) | Academic department |
| `enrollment_date` | Date | Date of enrollment |

## Tech Stack

- **Backend**: Flask 2.3.3, SQLAlchemy, Flask-Migrate
- **Frontend**: HTML5, CSS3, Bootstrap 5.3, Jinja2
- **Database**: SQLite (development), PostgreSQL ready
- **Forms**: WTForms with validation
- **Icons**: Font Awesome 6.0

## Development Features

- **Debug Mode**: Enabled for development
- **Auto-reload**: File changes trigger restart
- **Error Handling**: Comprehensive error management
- **Flash Messages**: User feedback system
- **Form Validation**: Client & server-side validation
- **Responsive Design**: Mobile-first approach

## Git Workflow

This project uses proper Git version control with meaningful commits:

```bash
# View commit history
git log --oneline

# Create feature branch
git checkout -b feature/new-feature

# Regular commits
git add .
git commit -m "Add feature description"

# Push to remote
git push origin main
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

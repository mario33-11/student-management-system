@echo off
REM ----------------------------------------
REM Run Student Management System Flask app and open browser
REM ----------------------------------------

REM Get project folder
set SCRIPT_DIR=%~dp0

REM Navigate to project folder
cd /d "%SCRIPT_DIR%"

REM Set Flask environment variables
set FLASK_APP=app.py
set FLASK_ENV=development

REM Run Flask in a separate window
start "" cmd /k "flask run"

REM Wait a few seconds to let Flask start
timeout /t 5 /nobreak > nul

REM Open default browser to Flask app
start http://127.0.0.1:5000

exit

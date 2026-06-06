@echo off
title Car Rental System
color 0A

echo ========================================
echo    CAR RENTAL SYSTEM
echo ========================================
echo.

:: Check if virtual environment exists
if not exist "venv\Scripts\activate" (
    echo First time setup: Creating virtual environment...
    py -m venv venv
    echo.
    echo Installing required packages...
    call venv\Scripts\activate
    pip install django pillow openpyxl
    echo.
    echo Setup complete!
)

:: Activate and run
echo Starting server...
echo.
echo Website: http://127.0.0.1:8000
echo Admin:   http://127.0.0.1:8000/admin
echo.
echo Keep this window open while using the system!
echo Close this window to stop the server.
echo.

call venv\Scripts\activate
py manage.py runserver

pause
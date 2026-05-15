# Python-MySQL-MedicalExam

Medical Service System – Developing Applications with Python (Exam SET01)

## Requirements

- Python 3.x
- MySQL (XAMPP / MAMP)
- `pip install mysql-connector-python`

## Setup

1. Run `medical_service.sql` in phpMyAdmin to create database and tables.
2. Edit `DB_PASSWORD` in `medical_service.py` if your MySQL password differs.
3. Run: `python main.py`

## Files

| File | Description |
|------|-------------|
| `main.py` | Main program |
| `medical_service.py` | Database connection and all functions (Q1–Q5) |
| `medical_service.sql` | Database schema |

## Exam functions

1. `connect_db()` – Connection to database
2. `add_patients_from_keyboard()` – Add 3 patients
3. `add_doctors_from_keyboard()` – Add 5 doctors
4. `add_appointments_from_keyboard()` – Add 3 appointments
5. `make_report()` – Appointment report
6. `get_appointments_today()` – Today's appointments

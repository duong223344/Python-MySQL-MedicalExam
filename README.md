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

## Exam marking schema (15 marks)

| Question | Marks | Function |
|----------|-------|----------|
| 1 Connection to database | 1 | `connect_db()` |
| 2 Insert patients | 3 | `add_patients_from_keyboard()` |
| 2 Insert doctors | 3 | `add_doctors_from_keyboard()` |
| 3 Insert appointments | 2 | `add_appointments_from_keyboard()` |
| 4 Make a report | 3 | `make_report()` |
| 5 Get appointments today | 2 | `get_appointments_today()` |
| Bonus coding convention | 1 | Clear structure, `%s`, try/except |

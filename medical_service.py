"""
Medical Service System
Developing Applications with Python - Exam SET01
"""

import mysql.connector
from mysql.connector import Error
from datetime import date

# MAMP: port 3306, user root, password root (Preferences -> Ports)
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "medical_service"


# ===========================================================================
# Question 1: Connection to database (1 mark)
# ===========================================================================
def connect_db():
    """Connect to MySQL database medical_service."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        if conn.is_connected():
            print("Connected to database: medical_service")
        return conn
    except Error as e:
        print(f"Connection error: {e}")
        return None


def format_birthday(dob):
    """Birthday column: show year only (2010, 1990) as in exam sample."""
    if dob is None:
        return ""
    if hasattr(dob, "year"):
        return str(dob.year)
    return str(dob)[:4]


def format_date(appt_date):
    """Format appointment datetime for report."""
    if appt_date is None:
        return ""
    if hasattr(appt_date, "strftime"):
        return appt_date.strftime("%Y-%m-%d")
    return str(appt_date)[:10]


# ===========================================================================
# Question 2: Add 3 patients from keyboard (3 marks)
# ===========================================================================
def add_patient(cursor):
    """Insert one patient from keyboard."""
    print("\n--- Patient ---")
    full_name = input("Full name: ").strip()
    date_of_birth = input("Date of birth (YYYY-MM-DD): ").strip()
    gender = input("Gender: ").strip()
    address = input("Address: ").strip()
    phone_number = input("Phone number: ").strip()
    email = input("Email: ").strip()

    sql = """
        INSERT INTO patients
            (full_name, date_of_birth, gender, address, phone_number, email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(
        sql,
        (full_name, date_of_birth, gender, address, phone_number, email),
    )
    print(f"Added patient. patient_id = {cursor.lastrowid}")


def add_patients_from_keyboard(cursor):
    """Add 3 patients from keyboard."""
    print("\n" + "=" * 60)
    print("QUESTION 2: ADD 3 PATIENTS")
    print("=" * 60)
    for i in range(1, 4):
        print(f"\nPatient {i}/3")
        add_patient(cursor)


# ===========================================================================
# Question 2: Add 5 doctors from keyboard (3 marks)
# ===========================================================================
def add_doctor(cursor):
    """Insert one doctor from keyboard."""
    print("\n--- Doctor ---")
    full_name = input("Full name: ").strip()
    specialization = input("Specialization: ").strip()
    phone_number = input("Phone number: ").strip()
    email = input("Email: ").strip()
    years_of_experience = int(input("Years of experience: ").strip())

    sql = """
        INSERT INTO doctors
            (full_name, specialization, phone_number, email, years_of_experience)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(
        sql,
        (full_name, specialization, phone_number, email, years_of_experience),
    )
    print(f"Added doctor. doctor_id = {cursor.lastrowid}")


def add_doctors_from_keyboard(cursor):
    """Add 5 doctors from keyboard."""
    print("\n" + "=" * 60)
    print("QUESTION 2: ADD 5 DOCTORS")
    print("=" * 60)
    for i in range(1, 6):
        print(f"\nDoctor {i}/5")
        add_doctor(cursor)


# ===========================================================================
# Question 3: Add 3 appointments for 3 patients (2 marks)
# ===========================================================================
def add_appointment(cursor, appointment_no):
    """Insert one appointment from keyboard (one appointment per patient)."""
    print(f"\n--- Appointment {appointment_no}/3 ---")
    patient_id = appointment_no  # 3 appointments for 3 patients (id 1, 2, 3)
    print(f"Patient ID: {patient_id}")
    doctor_id = int(input("Doctor ID: ").strip())
    appointment_date = input(
        "Appointment date (YYYY-MM-DD HH:MM:SS): "
    ).strip()
    reason = input("Reason: ").strip()
    status = input("Status (Pending/Done): ").strip()
    if not status:
        status = "Pending"

    sql = """
        INSERT INTO appointments
            (patient_id, doctor_id, appointment_date, reason, status)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(
        sql,
        (patient_id, doctor_id, appointment_date, reason, status),
    )
    print(f"Added appointment. appointment_id = {cursor.lastrowid}")


def add_appointments_from_keyboard(cursor):
    """Add 3 appointments for 3 patients from keyboard."""
    print("\n" + "=" * 60)
    print("QUESTION 3: ADD 3 APPOINTMENTS")
    print("=" * 60)
    for i in range(1, 4):
        add_appointment(cursor, i)


# ===========================================================================
# Question 4: Make a report and show to screen (3 marks)
# ===========================================================================
def make_report(cursor):
    """
    Report template:
    No | Patient name | Birthday | Gender | Address | Doctor name | Reason | Date
    """
    sql = """
        SELECT
            p.patient_id,
            p.full_name,
            p.date_of_birth,
            p.gender,
            p.address,
            d.full_name,
            a.reason,
            a.appointment_date
        FROM appointments a
        INNER JOIN patients p ON a.patient_id = p.patient_id
        INNER JOIN doctors d ON a.doctor_id = d.doctor_id
        ORDER BY p.patient_id
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    print("\n" + "=" * 90)
    print("QUESTION 4: APPOINTMENT REPORT")
    print("=" * 90)
    print(
        f"{'No':<4}{'Patient name':<14}{'Birthday':<10}{'Gender':<8}"
        f"{'Address':<10}{'Doctor name':<14}{'Reason':<12}{'Date'}"
    )
    print("-" * 90)

    for row in rows:
        no, pname, dob, gender, address, dname, reason, appt_date = row
        print(
            f"{no:<4}{pname:<14}{format_birthday(dob):<10}{gender:<8}"
            f"{(address or ''):<10}{(dname or ''):<14}{(reason or ''):<12}"
            f"{format_date(appt_date)}"
        )
    print("=" * 90)


# ===========================================================================
# Question 5: Get all appointments today and show to screen (2 marks)
# ===========================================================================
def get_appointments_today(cursor):
    """
    Today's appointments:
    Address | No | Patient name | Birthday | Gender | Doctor name | Status | Note
    """
    today = date.today()
    sql = """
        SELECT
            p.address,
            p.patient_id,
            p.full_name,
            p.date_of_birth,
            p.gender,
            d.full_name,
            a.status,
            a.reason
        FROM appointments a
        INNER JOIN patients p ON a.patient_id = p.patient_id
        INNER JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE DATE(a.appointment_date) = %s
        ORDER BY p.patient_id
    """
    cursor.execute(sql, (today,))
    rows = cursor.fetchall()

    print("\n" + "=" * 90)
    print(f"QUESTION 5: APPOINTMENTS TODAY ({today})")
    print("=" * 90)
    print(
        f"{'Address':<10}{'No':<4}{'Patient name':<14}{'Birthday':<10}"
        f"{'Gender':<8}{'Doctor name':<14}{'Status':<10}{'Note'}"
    )
    print("-" * 90)

    if not rows:
        print("No appointments today.")
    else:
        for row in rows:
            address, no, pname, dob, gender, dname, status, note = row
            print(
                f"{(address or ''):<10}{no:<4}{pname:<14}{format_birthday(dob):<10}"
                f"{gender:<8}{(dname or ''):<14}{(status or ''):<10}{(note or '')}"
            )
    print("=" * 90)

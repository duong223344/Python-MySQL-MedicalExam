"""
Main program - Medical Service System
Run: python main.py
"""

from mysql.connector import Error

from medical_service import (
    add_appointments_from_keyboard,
    add_doctors_from_keyboard,
    add_patients_from_keyboard,
    connect_db,
    get_appointments_today,
    make_report,
)


def main():
    print("MEDICAL SERVICE SYSTEM")
    print("Developing Applications with Python - Exam SET01\n")

    # Question 1
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()

    try:
        # Question 2
        add_patients_from_keyboard(cursor)
        add_doctors_from_keyboard(cursor)
        conn.commit()

        # Question 3
        add_appointments_from_keyboard(cursor)
        conn.commit()

        # Question 4
        make_report(cursor)

        # Question 5
        get_appointments_today(cursor)

    except Error as e:
        print(f"Database error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
        print("\nConnection closed.")


if __name__ == "__main__":
    main()

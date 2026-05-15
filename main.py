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


def show_menu():
    """Display main menu."""
    print("\n" + "=" * 50)
    print("  MEDICAL SERVICE SYSTEM - MENU")
    print("=" * 50)
    print("  1. Add 3 patients (Question 2)")
    print("  2. Add 5 doctors (Question 2)")
    print("  3. Add 3 appointments (Question 3)")
    print("  4. Appointment report (Question 4)")
    print("  5. Today's appointments (Question 5)")
    print("  6. Run all (Q2 -> Q3 -> Q4 -> Q5)")
    print("  0. Exit")
    print("=" * 50)


def run_all(cursor, conn):
    """Run full exam flow."""
    add_patients_from_keyboard(cursor)
    add_doctors_from_keyboard(cursor)
    conn.commit()
    add_appointments_from_keyboard(cursor)
    conn.commit()
    make_report(cursor)
    get_appointments_today(cursor)


def main():
    print("MEDICAL SERVICE SYSTEM")
    print("Developing Applications with Python - Exam SET01\n")

    # Question 1: Connection to database
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()

    try:
        while True:
            show_menu()
            choice = input("Choose option (0-6): ").strip()

            if choice == "0":
                print("Goodbye!")
                break

            try:
                if choice == "1":
                    add_patients_from_keyboard(cursor)
                    conn.commit()
                    print("Saved 3 patients.")

                elif choice == "2":
                    add_doctors_from_keyboard(cursor)
                    conn.commit()
                    print("Saved 5 doctors.")

                elif choice == "3":
                    add_appointments_from_keyboard(cursor)
                    conn.commit()
                    print("Saved 3 appointments.")

                elif choice == "4":
                    make_report(cursor)

                elif choice == "5":
                    get_appointments_today(cursor)

                elif choice == "6":
                    run_all(cursor, conn)

                else:
                    print("Invalid option. Please choose 0-6.")

            except Error as e:
                print(f"Database error: {e}")
                conn.rollback()

    finally:
        cursor.close()
        conn.close()
        print("\nConnection closed.")


if __name__ == "__main__":
    main()

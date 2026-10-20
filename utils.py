from datetime import date, datetime


def required_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field is required.")


def positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt).strip())

            if value > 0:
                return value

            print("Enter a number greater than zero.")

        except ValueError:
            print("Enter a valid whole number.")


def choose_blood_group():
    from config import BLOOD_GROUPS

    print("Available blood groups:", ", ".join(BLOOD_GROUPS))

    while True:
        group = input("Enter blood group: ").strip().upper()

        if group in BLOOD_GROUPS:
            return group

        print("Invalid blood group. Please try again.")


def valid_phone(prompt="Enter phone number: "):
    while True:
        phone = input(prompt).strip()

        if phone.isdigit() and 7 <= len(phone) <= 15:
            return phone

        print("Enter 7 to 15 digits without spaces or symbols.")


def input_date(prompt="Enter date YYYY-MM-DD (blank for today): "):
    while True:
        value = input(prompt).strip()

        if not value:
            return date.today().isoformat()

        try:
            parsed = datetime.strptime(value, "%Y-%m-%d").date()

            if parsed > date.today():
                print("Future dates are not allowed.")
                continue

            return parsed.isoformat()

        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format.")


def pause():
    input("\nPress Enter to continue...")

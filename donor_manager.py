from config import DONORS_FILE
from storage import read_data, write_data
from utils import required_input, choose_blood_group, valid_phone


def add_donor():
    donors = read_data(DONORS_FILE)

    name = required_input("Enter donor full name: ")
    phone = valid_phone()

    if any(
        donor["phone"] == phone and donor["active"]
        for donor in donors
    ):
        print("An active donor with this phone number already exists.")
        return

    age_text = required_input("Enter donor age: ")

    try:
        age = int(age_text)
    except ValueError:
        print("Age must be a whole number.")
        return

    if not 18 <= age <= 120:
        print("This demo registers donors aged 18 to 120.")
        return

    blood_group = choose_blood_group()
    city = required_input("Enter city: ")

    donor_id = max(
        (donor["id"] for donor in donors),
        default=0
    ) + 1

    donors.append({
        "id": donor_id,
        "name": name,
        "phone": phone,
        "age": age,
        "blood_group": blood_group,
        "city": city,
        "active": True
    })

    write_data(DONORS_FILE, donors)

    print(f"Donor registered successfully. Donor ID: {donor_id}")


def list_donors():
    donors = read_data(DONORS_FILE)

    if not donors:
        print("No donors registered.")
        return

    print("\n" + "-" * 90)
    print(
        f"{'ID':<6}{'Name':<24}{'Phone':<17}"
        f"{'Age':<8}{'Group':<10}{'City':<18}{'Status':<10}"
    )
    print("-" * 90)

    for donor in donors:
        status = "Active" if donor["active"] else "Inactive"

        print(
            f"{donor['id']:<6}"
            f"{donor['name'][:23]:<24}"
            f"{donor['phone']:<17}"
            f"{donor['age']:<8}"
            f"{donor['blood_group']:<10}"
            f"{donor['city'][:17]:<18}"
            f"{status:<10}"
        )


def search_donor():
    donors = read_data(DONORS_FILE)
    query = required_input("Search by donor ID, name, or phone: ").lower()

    matches = [
        donor for donor in donors
        if query == str(donor["id"])
        or query in donor["name"].lower()
        or query in donor["phone"].lower()
    ]

    if not matches:
        print("No matching donors found.")
        return

    for donor in matches:
        print("-" * 35)
        print(f"Donor ID: {donor['id']}")
        print(f"Name: {donor['name']}")
        print(f"Phone: {donor['phone']}")
        print(f"Age: {donor['age']}")
        print(f"Blood group: {donor['blood_group']}")
        print(f"City: {donor['city']}")
        print(f"Status: {'Active' if donor['active'] else 'Inactive'}")


def deactivate_donor():
    donors = read_data(DONORS_FILE)
    donor_id = int(required_input("Enter donor ID to deactivate: "))

    donor = next(
        (item for item in donors if item["id"] == donor_id),
        None
    )

    if not donor:
        print("Donor not found.")
        return

    if not donor["active"]:
        print("This donor is already inactive.")
        return

    confirmation = input(
        f"Deactivate donor {donor['name']}? Type YES to confirm: "
    ).strip()

    if confirmation != "YES":
        print("Operation cancelled.")
        return

    donor["active"] = False
    write_data(DONORS_FILE, donors)

    print("Donor deactivated successfully.")

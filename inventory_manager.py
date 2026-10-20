from config import (
    DONORS_FILE,
    DONATIONS_FILE,
    INVENTORY_FILE
)
from storage import read_data, write_data
from utils import (
    positive_integer,
    choose_blood_group,
    input_date
)


def get_stock(group):
    inventory = read_data(INVENTORY_FILE)

    item = next(
        (entry for entry in inventory if entry["blood_group"] == group),
        None
    )

    return item["units"] if item else 0


def change_stock(group, amount):
    inventory = read_data(INVENTORY_FILE)

    item = next(
        (entry for entry in inventory if entry["blood_group"] == group),
        None
    )

    if not item:
        item = {"blood_group": group, "units": 0}
        inventory.append(item)

    new_units = item["units"] + amount

    if new_units < 0:
        return False

    item["units"] = new_units
    write_data(INVENTORY_FILE, inventory)
    return True


def record_donation():
    donors = read_data(DONORS_FILE)
    donations = read_data(DONATIONS_FILE)

    donor_id = positive_integer("Enter donor ID: ")

    donor = next(
        (
            item for item in donors
            if item["id"] == donor_id and item["active"]
        ),
        None
    )

    if not donor:
        print("Active donor not found.")
        return

    print(f"Donor: {donor['name']}")
    print(f"Registered blood group: {donor['blood_group']}")

    group = choose_blood_group()

    if group != donor["blood_group"]:
        print("Blood group does not match the donor record.")
        return

    units = positive_integer(
        "Enter units recorded (whole units for this demo): "
    )

    donation_date = input_date()

    donation_id = max(
        (donation["id"] for donation in donations),
        default=0
    ) + 1

    # Keep the donation record and inventory update together as a
    # single logical operation, and write the donation log first.
    donation = {
        "id": donation_id,
        "donor_id": donor_id,
        "donor_name": donor["name"],
        "blood_group": group,
        "units": units,
        "date": donation_date
    }

    donations.append(donation)
    write_data(DONATIONS_FILE, donations)

    try:
        if not change_stock(group, units):
            donations.pop()
            write_data(DONATIONS_FILE, donations)
            print("Could not update inventory.")
            return
    except (OSError, ValueError):
        donations.pop()
        write_data(DONATIONS_FILE, donations)
        raise

    print(f"Donation recorded. Donation ID: {donation_id}")
    print(f"Demo inventory for {group}: {get_stock(group)} units")


def show_inventory():
    inventory = read_data(INVENTORY_FILE)

    print("\nBLOOD INVENTORY")
    print("-" * 35)
    print(f"{'Blood Group':<18}{'Units':>10}")
    print("-" * 35)

    for item in inventory:
        print(f"{item['blood_group']:<18}{item['units']:>10}")

    print("-" * 35)
    print(
        f"{'Total units':<18}"
        f"{sum(item['units'] for item in inventory):>10}"
    )


def donation_history():
    donations = read_data(DONATIONS_FILE)

    if not donations:
        print("No donation records found.")
        return

    print("\nDONATION HISTORY")
    print("-" * 80)

    for donation in sorted(donations, key=lambda item: item["date"]):
        print(
            f"ID: {donation['id']} | "
            f"Donor: {donation['donor_name']} | "
            f"Group: {donation['blood_group']} | "
            f"Units: {donation['units']} | "
            f"Date: {donation['date']}"
        )

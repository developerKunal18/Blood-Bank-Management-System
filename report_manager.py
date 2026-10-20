from config import (
    DONORS_FILE,
    DONATIONS_FILE,
    INVENTORY_FILE,
    REQUESTS_FILE
)
from storage import read_data


def dashboard():
    donors = read_data(DONORS_FILE)
    donations = read_data(DONATIONS_FILE)
    inventory = read_data(INVENTORY_FILE)
    requests = read_data(REQUESTS_FILE)

    active_donors = sum(1 for donor in donors if donor["active"])
    total_units = sum(item["units"] for item in inventory)

    pending_requests = sum(
        1 for request in requests
        if request["status"] == "Pending"
    )

    fulfilled_requests = sum(
        1 for request in requests
        if request["status"] == "Fulfilled"
    )

    print("\n" + "=" * 45)
    print("       BLOOD BANK DASHBOARD")
    print("=" * 45)
    print(f"Total registered donors: {len(donors)}")
    print(f"Active donors:           {active_donors}")
    print(f"Donation records:        {len(donations)}")
    print(f"Inventory units:         {total_units}")
    print(f"Total requests:          {len(requests)}")
    print(f"Pending requests:        {pending_requests}")
    print(f"Fulfilled requests:      {fulfilled_requests}")
    print("=" * 45)


def low_stock_report():
    inventory = read_data(INVENTORY_FILE)

    # This is a configurable demonstration threshold, not a clinical standard.
    threshold = 5

    print(f"\nLOW STOCK REPORT — fewer than {threshold} units")
    print("-" * 40)

    low_stock = [
        item for item in inventory
        if item["units"] < threshold
    ]

    if not low_stock:
        print("No blood groups are below the demo threshold.")
        return

    for item in low_stock:
        print(f"{item['blood_group']}: {item['units']} units")


def request_summary():
    requests = read_data(REQUESTS_FILE)

    if not requests:
        print("No request records available.")
        return

    print("\nREQUEST SUMMARY BY BLOOD GROUP")
    print("-" * 45)

    for group in ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"):
        matching = [
            request for request in requests
            if request["blood_group"] == group
        ]

        if not matching:
            continue

        pending = sum(
            request["units"] for request in matching
            if request["status"] == "Pending"
        )

        fulfilled = sum(
            request["units"] for request in matching
            if request["status"] == "Fulfilled"
        )

        print(
            f"{group:<5} | Requests: {len(matching):<4} | "
            f"Pending units: {pending:<5} | Fulfilled units: {fulfilled}"
        )

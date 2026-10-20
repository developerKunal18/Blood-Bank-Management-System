from config import REQUESTS_FILE, INVENTORY_FILE
from storage import read_data, write_data
from utils import (
    required_input,
    positive_integer,
    choose_blood_group,
    input_date
)


def create_request():
    requests = read_data(REQUESTS_FILE)

    patient_name = required_input("Enter patient/reference name: ")
    hospital = required_input("Enter hospital name: ")
    group = choose_blood_group()
    units = positive_integer("Enter requested units: ")
    request_date = input_date()

    request_id = max(
        (request["id"] for request in requests),
        default=0
    ) + 1

    request = {
        "id": request_id,
        "patient_name": patient_name,
        "hospital": hospital,
        "blood_group": group,
        "units": units,
        "date": request_date,
        "status": "Pending",
        "fulfilled_date": None
    }

    requests.append(request)
    write_data(REQUESTS_FILE, requests)

    print(f"Request registered successfully. Request ID: {request_id}")
    print("The request remains pending until fulfilled.")


def list_requests():
    requests = read_data(REQUESTS_FILE)

    if not requests:
        print("No blood requests found.")
        return

    print("\nBLOOD REQUESTS")
    print("-" * 90)

    for request in sorted(requests, key=lambda item: item["id"]):
        print(
            f"Request ID: {request['id']}\n"
            f"Reference: {request['patient_name']}\n"
            f"Hospital: {request['hospital']}\n"
            f"Blood group: {request['blood_group']}\n"
            f"Units requested: {request['units']}\n"
            f"Request date: {request['date']}\n"
            f"Status: {request['status']}\n"
            f"{'-' * 90}"
        )


def fulfill_request():
    requests = read_data(REQUESTS_FILE)
    inventory = read_data(INVENTORY_FILE)

    request_id = positive_integer("Enter pending request ID: ")

    request = next(
        (
            item for item in requests
            if item["id"] == request_id and item["status"] == "Pending"
        ),
        None
    )

    if not request:
        print("Pending request not found.")
        return

    stock_item = next(
        (
            item for item in inventory
            if item["blood_group"] == request["blood_group"]
        ),
        None
    )

    available = stock_item["units"] if stock_item else 0

    print(f"Requested group: {request['blood_group']}")
    print(f"Requested units: {request['units']}")
    print(f"Available demo stock: {available}")

    if available < request["units"]:
        print("Insufficient stock. Request remains pending.")
        return

    confirmation = input(
        "Confirm fulfilment in this demo? Type YES: "
    ).strip()

    if confirmation != "YES":
        print("Operation cancelled.")
        return

    stock_item["units"] -= request["units"]
    request["status"] = "Fulfilled"
    request["fulfilled_date"] = input_date()

    # Persist the updated stock and request status.
    write_data(INVENTORY_FILE, inventory)

    try:
        write_data(REQUESTS_FILE, requests)
    except OSError:
        # Best-effort rollback of stock if the request log cannot be saved.
        stock_item["units"] += request["units"]
        write_data(INVENTORY_FILE, inventory)
        raise

    print("Request marked fulfilled in the demo system.")
    print("Real blood issue must be authorized by qualified blood-bank staff.")

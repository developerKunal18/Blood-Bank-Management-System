from storage import initialize_storage
from donor_manager import (
    add_donor,
    list_donors,
    search_donor,
    deactivate_donor
)
from inventory_manager import (
    record_donation,
    show_inventory,
    donation_history
)
from request_manager import (
    create_request,
    list_requests,
    fulfill_request
)
from report_manager import (
    dashboard,
    low_stock_report,
    request_summary
)
from utils import pause


def show_menu():
    print("\n" + "=" * 48)
    print("       BLOOD BANK MANAGEMENT SYSTEM")
    print("=" * 48)
    print("1.  Dashboard")
    print("2.  Register Donor")
    print("3.  View Donors")
    print("4.  Search Donor")
    print("5.  Deactivate Donor")
    print("6.  Record Donation")
    print("7.  View Blood Inventory")
    print("8.  View Donation History")
    print("9.  Create Blood Request")
    print("10. View Blood Requests")
    print("11. Fulfil Blood Request")
    print("12. Low Stock Report")
    print("13. Request Summary")
    print("0.  Exit")
    print("=" * 48)


def main():
    initialize_storage()

    actions = {
        "1": dashboard,
        "2": add_donor,
        "3": list_donors,
        "4": search_donor,
        "5": deactivate_donor,
        "6": record_donation,
        "7": show_inventory,
        "8": donation_history,
        "9": create_request,
        "10": list_requests,
        "11": fulfill_request,
        "12": low_stock_report,
        "13": request_summary
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using Blood Bank Management System.")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (OSError, ValueError, KeyError, TypeError) as error:
                print(f"Operation failed: {error}")
        else:
            print("Invalid choice. Select a number from the menu.")

        pause()


if __name__ == "__main__":
    main()

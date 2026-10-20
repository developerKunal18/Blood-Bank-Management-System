# Blood Bank Management System

A beginner-friendly Python project for maintaining donor records, recording donations, tracking blood inventory, and managing blood requests.

## Features

- Register and search blood donors
- View and deactivate donor records
- Record blood donations
- Maintain stock for eight blood groups
- Create blood requests
- Fulfil requests when sufficient demo inventory is available
- Track donation and request histories
- Generate low-stock reports
- View dashboard statistics and request summaries
- Store information in JSON files

## Technologies Used

- Python
- JSON
- Python standard library

## Requirements

- Python 3.10 or newer recommended
- VS Code or another Python editor

No third-party libraries or database server are required.

## Project Structure

```text
BloodBankManagementSystem/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── donor_manager.py
├── inventory_manager.py
├── request_manager.py
├── report_manager.py
├── requirements.txt
├── .gitignore
└── data/
    ├── donors.json
    ├── donations.json
    ├── inventory.json
    └── requests.json
```

## Installation and Execution

1. Download or clone the repository.
2. Open the project folder in VS Code.
3. Ensure the `data` folder and JSON files exist.
4. Open a terminal in the project directory.
5. Run the application:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

The application initializes missing data files automatically.

## How to Use

1. Register a donor and select their blood group.
2. Record a donation against the donor's registered blood group.
3. View the inventory to check the recorded stock.
4. Create a blood request for a hospital or patient reference.
5. Fulfil a pending request if sufficient demo stock is available.
6. Review donation history, pending requests, and reports.

## Data Storage

All information is stored locally in JSON files inside the `data` directory. Back up these files regularly.

## Important Disclaimer

This is an educational demonstration, not a production blood-bank system. Its stock figures are simplified inventory units and do not represent verified, tested, screened, or clinically compatible blood components. Real donation eligibility, testing, storage, compatibility, issue, and transfusion decisions must be handled by qualified blood-bank professionals under applicable procedures.

The project does not include authentication, access control, audit-grade transactions, or patient-data protections required for real-world deployment.

## Future Improvements

- Add a Tkinter graphical interface
- Connect to MySQL
- Add administrator login and role-based permissions
- Export reports to CSV
- Add donation eligibility reminders
- Add a database-backed audit log

## Author

Kunal Karbhari

## License

For educational and personal learning purposes.

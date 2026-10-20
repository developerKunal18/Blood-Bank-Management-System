from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

DONORS_FILE = DATA_DIR / "donors.json"
DONATIONS_FILE = DATA_DIR / "donations.json"
INVENTORY_FILE = DATA_DIR / "inventory.json"
REQUESTS_FILE = DATA_DIR / "requests.json"

BLOOD_GROUPS = [
    "A+", "A-", "B+", "B-",
    "AB+", "AB-", "O+", "O-"
]

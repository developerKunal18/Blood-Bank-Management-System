import json
from config import (
    DATA_DIR,
    DONORS_FILE,
    DONATIONS_FILE,
    INVENTORY_FILE,
    REQUESTS_FILE,
    BLOOD_GROUPS
)


def initialize_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    defaults = {
        DONORS_FILE: [],
        DONATIONS_FILE: [],
        INVENTORY_FILE: [
            {"blood_group": group, "units": 0}
            for group in BLOOD_GROUPS
        ],
        REQUESTS_FILE: []
    }

    for path, default_data in defaults.items():
        if not path.exists():
            with open(path, "w", encoding="utf-8") as file:
                json.dump(default_data, file, indent=4)


def read_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError(
                f"{file_path.name} must contain a JSON list."
            )

        return data

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as error:
        raise ValueError(
            f"{file_path.name} contains invalid JSON."
        ) from error


def write_data(file_path, data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    temporary_path = file_path.with_suffix(".tmp")

    with open(temporary_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    temporary_path.replace(file_path)

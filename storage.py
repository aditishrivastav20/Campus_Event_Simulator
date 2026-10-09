import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
EVENTS_FILE = DATA_DIR / "events.json"
REGISTRATIONS_FILE = DATA_DIR / "registrations.json"


def load_data(file_path):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print(f"Warning: Could not read {file_path.name}.")
        return []


def save_data(file_path, data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    temporary_file = file_path.with_suffix(".tmp")

    try:
        with temporary_file.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        temporary_file.replace(file_path)
        return True

    except OSError:
        print(f"Error: Could not save {file_path.name}.")
        temporary_file.unlink(missing_ok=True)
        return False
import csv

from pathlib import Path

from event_service import (
    add_event,
    register_participant,
    cancel_registration,
    get_events,
    get_registrations,
)

from logger_config import logger


BASE_DIR = Path(__file__).parent
ATTENDANCE_FILE = BASE_DIR / "data" / "attendance.csv"


def export_attendance():
    registrations = get_registrations()

    try:
        ATTENDANCE_FILE.parent.mkdir(parents=True, exist_ok=True)

        with ATTENDANCE_FILE.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:
            fieldnames = [
                "participant_id",
                "name",
                "email",
                "mobile",
                "event_id",
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
            )

            writer.writeheader()
            writer.writerows(registrations)

        print(f"Attendance exported to {ATTENDANCE_FILE.name}")

    except OSError:
        print("Could not export attendance.")


def main():
    while True:
        print("\n===== CAMPUS EVENT REGISTRATION =====")
        print("1. Add Event")
        print("2. View Events")
        print("3. Register Participant")
        print("4. Cancel Registration")
        print("5. View Registrations")
        print("6. Export Attendance CSV")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            event_id = input("Event ID: ").strip()
            event_name = input("Event name: ").strip()

            try:
                capacity = int(input("Maximum participants: "))
            except ValueError:
                print("Capacity must be a number.")
                continue

            success, message = add_event(
                event_id,
                event_name,
                capacity,
            )

            print(message)

        elif choice == "2":
            events = get_events()

            if not events:
                print("No events found.")
            else:
                for event in events:
                    print(
                        f'{event["event_id"]} | '
                        f'{event["event_name"]} | '
                        f'Capacity: {event["capacity"]}'
                    )

        elif choice == "3":
            participant_id = input("Participant ID (P001): ").strip()
            name = input("Participant name: ").strip()
            email = input("Email: ").strip()
            mobile = input("Mobile number: ").strip()
            event_id = input("Event ID: ").strip()

            success, message = register_participant(
                participant_id,
                name,
                email,
                mobile,
                event_id,
            )

            print(message)

        elif choice == "4":
            participant_id = input("Participant ID: ").strip()
            event_id = input("Event ID: ").strip()

            success, message = cancel_registration(
                participant_id,
                event_id,
            )

            print(message)

        elif choice == "5":
            registrations = get_registrations()

            if not registrations:
                print("No registrations found.")
            else:
                for registration in registrations:
                    print(
                        f'{registration["participant_id"]} | '
                        f'{registration["name"]} | '
                        f'{registration["event_id"]}'
                    )

        elif choice == "6":
            export_attendance()

        elif choice == "7":
            logger.info("Application closed.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
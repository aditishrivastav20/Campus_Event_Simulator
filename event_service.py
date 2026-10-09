from storage import (
    DATA_DIR,
    EVENTS_FILE,
    REGISTRATIONS_FILE,
    load_data,
    save_data,
)

from validators import (
    validate_participant_id,
    validate_email,
    validate_mobile,
)

from logger_config import logger


def add_event(event_id, event_name, capacity):
    events = load_data(EVENTS_FILE)

    if any(event["event_id"] == event_id for event in events):
        return False, "Event ID already exists."

    if not event_id.strip() or not event_name.strip():
        return False, "Event ID and name are required."

    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        return False, "Capacity must be a positive integer."

    event = {
        "event_id": event_id,
        "event_name": event_name,
        "capacity": capacity,
    }

    events.append(event)

    if not save_data(EVENTS_FILE, events):
        return False, "Could not save event."

    logger.info("Event created: %s", event_id)
    return True, "Event created successfully."


def register_participant(participant_id, name, email, mobile, event_id):
    events = load_data(EVENTS_FILE)
    registrations = load_data(REGISTRATIONS_FILE)

    if not validate_participant_id(participant_id):
        return False, "Invalid participant ID. Example: P001."

    if not name.strip():
        return False, "Name is required."

    if not validate_email(email):
        return False, "Invalid email address."

    if not validate_mobile(mobile):
        return False, "Invalid Indian mobile number."

    event = next(
        (item for item in events if item["event_id"] == event_id),
        None
    )

    if event is None:
        return False, "Event not found."

    for registration in registrations:
        if registration["participant_id"] == participant_id:
            if registration["event_id"] == event_id:
                return False, "Already registered for this event."

    event_registrations = [
        registration
        for registration in registrations
        if registration["event_id"] == event_id
    ]

    if len(event_registrations) >= event["capacity"]:
        return False, "Event is full."

    participant = {
        "participant_id": participant_id,
        "name": name.strip(),
        "email": email.strip(),
        "mobile": mobile,
        "event_id": event_id,
    }

    registrations.append(participant)

    if not save_data(REGISTRATIONS_FILE, registrations):
        return False, "Could not save registration."

    logger.info(
        "Registration successful: %s for %s",
        participant_id,
        event_id,
    )

    return True, "Registration successful."


def cancel_registration(participant_id, event_id):
    registrations = load_data(REGISTRATIONS_FILE)

    updated_registrations = [
        registration
        for registration in registrations
        if not (
            registration["participant_id"] == participant_id
            and registration["event_id"] == event_id
        )
    ]

    if len(updated_registrations) == len(registrations):
        return False, "Registration not found."

    if not save_data(REGISTRATIONS_FILE, updated_registrations):
        return False, "Could not save cancellation."

    logger.info(
        "Registration cancelled: %s for %s",
        participant_id,
        event_id,
    )

    return True, "Registration cancelled successfully."


def get_events():
    return load_data(EVENTS_FILE)


def get_registrations(event_id=None):
    registrations = load_data(REGISTRATIONS_FILE)

    if event_id is None:
        return registrations

    return [
        registration
        for registration in registrations
        if registration["event_id"] == event_id
    ]
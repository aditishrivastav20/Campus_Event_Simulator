import re


def validate_participant_id(participant_id):
    return bool(re.fullmatch(r"P\d{3,}", participant_id))


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))


def validate_mobile(mobile):
    return bool(re.fullmatch(r"[6-9]\d{9}", mobile))
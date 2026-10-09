import unittest

from validators import (
    validate_participant_id,
    validate_email,
    validate_mobile
)


class TestValidators(unittest.TestCase):

    def test_valid_participant_id(self):
        self.assertTrue(validate_participant_id("P001"))

    def test_invalid_participant_id(self):
        self.assertFalse(validate_participant_id("ABC"))

    def test_valid_email(self):
        self.assertTrue(validate_email("aditi@gmail.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_email("aditi123"))

    def test_valid_mobile(self):
        self.assertTrue(validate_mobile("9876543210"))

    def test_invalid_mobile(self):
        self.assertFalse(validate_mobile("12345"))


if __name__ == "__main__":
    unittest.main()
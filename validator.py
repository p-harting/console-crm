import re


class Validator:
    @staticmethod
    def validate_email(value):
        """
        Validates if the provided value matches a standard email format.

        :param value: The value (string) to be validated.
        :return: True if the value matches the email format, False otherwise.
        """
        return bool(re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', value))

    @staticmethod
    def backslash(value):
        """
        Checks if the provided value is exactly '/'.

        :param value: The value (string) to be checked.
        :return: True if the value is '/', False otherwise.
        """
        return value == "/"

    @staticmethod
    def not_empty(value):
        """
        Checks if the provided value is not empty (i.e., evaluates to True).

        :param value: The value (string or any object) to be checked.
        :return: True if the value is not empty, False otherwise.
        """
        return bool(value)

    @staticmethod
    def max_length(value):
        """
        Checks if the length of the provided value does not exceed 128 chars.

        :param value: The value (string) to be checked.
        :return: True if the length of the value is 128 characters or less,
                    False otherwise.
        """
        return len(value) <= 128

    @staticmethod
    def validate_dob(value):
        """
        Checks if the provided value matches this date format (YYYY/MM/DD).

        :param value: The value (string) to be checked.
        :return: True if the value matches the date of birth format,
                    False otherwise.
        """
        return bool(re.match(r'^\d{4}/\d{2}/\d{2}$', value))

    @staticmethod
    def validate_phone(value):
        """
        Validates if the provided value matches the amercian
        phone format (XXX-XXX-XXXX).

        :param value: The value (string) to be validated.
        :return: True if the value matches the phone number format,
                    False otherwise.
        """
        return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', value))

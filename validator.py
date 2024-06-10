import re
from datetime import datetime

class Validator:
    @staticmethod
    def validate_email(value):
        return bool(re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', value))
    @staticmethod
    def backslash(value):
        return value == "/"
    @staticmethod
    def not_empty(value):
        return bool(value)
    @staticmethod
    def max_length(value):
        return len(value) <= 128
    @staticmethod
    def validate_dob(value):
        return bool(re.match(r'^\d{4}/\d{2}/\d{2}$', value))
    @staticmethod
    def validate_phone(value):
        return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', value))
import re
from datetime import datetime

class Validator:
    @staticmethod
    def validate_email(value):
        return bool(re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', value))
    @staticmethod
    def backslash(value):
        return bool(value == "/")
    @staticmethod
    def not_empty(value):
        return bool(value)
    @staticmethod
    def max_length(value):
        return len(value) <= 24
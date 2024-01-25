import re


def normalize_phone(phone_number):
    """converting phone numbers into the correct format"""
    pattern = r"[\+\d]+"
    sanitized_numbers = "".join(re.findall(pattern, phone_number))
    if sanitized_numbers.startswith("380"):
        sanitized_numbers = "+" + sanitized_numbers
    elif sanitized_numbers.startswith("0"):
        sanitized_numbers = "+38" + sanitized_numbers
    return sanitized_numbers


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS sending:", sanitized_numbers)

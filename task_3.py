import re

def normalize_phone_contactats(raw_numbers):
    for number in raw_numbers:
        clean_number = re.sub(r'\D', '', number)
        if not clean_number.startswith('+'):
            if clean_number.startswith('380'):
                clean_number = '+' + clean_number
            else:
                clean_number = '+38' + clean_number
        return clean_number


print(normalize_phone_contactats([
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",]))
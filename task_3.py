import re

def normalize_phone(phone_number:str):
    sanitized_numbers = re.sub(r'\D', '', phone_number)
    if not sanitized_numbers.startswith('+'):
        if sanitized_numbers.startswith('380'):
            sanitized_numbers = '+' + sanitized_numbers
        else:
            sanitized_numbers = '+38' + sanitized_numbers
    return sanitized_numbers


print(normalize_phone("067\\t123 4567     "))
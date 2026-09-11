import random
import string

def generate_email(first_name: str, last_name: str, cohort_number: int) -> str:
    digits = ''.join(random.choices(string.digits, k=3))
    return f"{first_name}_{last_name}_{cohort_number}_{digits}@yandex.ru"

def generate_password(length: int = 8) -> str:
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))
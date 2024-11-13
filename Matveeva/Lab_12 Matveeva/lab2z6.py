import re

def is_valid_email(email):
    # Регулярное выражение для проверки корректности email адреса
    pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    return bool(pattern.match(email))

# Пример использования
email_input = input("Введите email адрес для проверки: ")
if is_valid_email(email_input):
    print("True")
else:
    print("False")
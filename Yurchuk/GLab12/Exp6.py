import re

def validate_email(email):
    """
    Функция для проверки корректности email адреса.

    :param email: строка, представляющая email адрес
    :return: True, если email корректен, иначе False
    """
    # Регулярное выражение для проверки email адреса
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))

# Пример использования
email = input("Введите email адрес для проверки: ")
if validate_email(email):
    print("Email адрес корректен.")
else:
    print("Email адрес некорректен.")
import re

def is_valid_url(url):
    # Регулярное выражение для проверки корректности URL
    pattern = re.compile(
        r'^(http|https)://'  # Протокол
        r'([a-zA-Z0-9.-]+)'  # Домен
        r'(\.[a-zA-Z]{2,})'   # Домен верхнего уровня
        r'(/.*)?$'            # Путь (необязательный)
    )
    return bool(pattern.match(url))

# Пример использования
url_input = input("Введите URL для проверки: ")
if is_valid_url(url_input):
    print("True")
else:
    print("False")
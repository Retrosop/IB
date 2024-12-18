import re

def find_unique_emails(file_path):
    """
    Функция для поиска уникальных email адресов в текстовом файле.

    :param file_path: путь к текстовому файлу
    :return: список уникальных email адресов
    """
    try:
        # Чтение содержимого файла
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Регулярное выражение для поиска email адресов
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, text)

        # Возвращаем уникальные email адреса
        unique_emails = list(set(emails))
        return unique_emails

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []

# Пример использования
file_path = 'D:\Python_progects\GLab12\input.txt'
unique_emails = find_unique_emails(file_path)

if unique_emails:
    print("Найденные уникальные email адреса:")
    for email in unique_emails:
        print(email)
else:
    print("Email адресов не найдено.")
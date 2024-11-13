import re

def find_unique_emails(file_path):
    # Регулярное выражение для поиска email адресов
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
    unique_emails = set()  # Используем множество для хранения уникальных email адресов

    # Чтение текстового файла
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Находим все email адреса в строке
            emails = email_pattern.findall(line)
            unique_emails.update(emails)  # Добавляем найденные email адреса в множество

    return list(unique_emails)  # Преобразуем множество в список для возврата

# Пример использования
file_path = input("Введите путь к текстовому файлу: ")
unique_emails = find_unique_emails(file_path)

# Вывод уникальных email адресов
if unique_emails:
    print("Найденные уникальные email адреса:")
    for email in unique_emails:
        print(email)
else:
    print("Email адреса не найдены.")
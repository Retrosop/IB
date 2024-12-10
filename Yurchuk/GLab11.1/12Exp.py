import csv
from collections import Counter


def create_password_dictionary(file_path, max_size=None, sort_desc=False):
    # Считываем пароли из файла CSV с указанием кодировки
    with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        passwords = [row[0] for row in reader]  # Предполагается, что пароли находятся в первом столбце

    # Подсчитываем количество вхождений каждого пароля
    password_counts = Counter(passwords)

    # Преобразуем в словарь
    password_dict = dict(password_counts)

    # Сортируем по количеству вхождений, если это необходимо
    if sort_desc:
        password_dict = dict(sorted(password_dict.items(), key=lambda item: item[1], reverse=True))

    # Ограничиваем размер словаря, если это необходимо
    if max_size is not None:
        password_dict = dict(list(password_dict.items())[:max_size])

    return password_dict

# Пример использования
file_path = r'D:\Python_progects\GLab11.1\leaked_passwords.csv'
password_dict = create_password_dictionary(file_path, max_size=10, sort_desc=True)
for password, count in password_dict.items():
    print(f"{password}: {count}")

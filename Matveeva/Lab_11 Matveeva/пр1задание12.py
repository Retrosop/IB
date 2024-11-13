import csv
from collections import Counter

def create_password_dictionary(file_path):
    """Создает словарь паролей на основе файла утечки."""
    password_counter = Counter()

    # Чтение файла CSV
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Проверяем, что строка не пустая
                password = row[0]  # Предполагаем, что пароль находится в первой колонке
                password_counter[password] += 1

    return dict(password_counter)

def main():
    file_path = input("Введите путь до файла утечки (CSV): ")  # Запрашиваем путь к файлу

    try:
        password_dict = create_password_dictionary(file_path)
        for password, count in password_dict.items():
            print(f"{password}: {count}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
import re
import argparse

def get_phone_pattern(lang):
    """
    Возвращает регулярное выражение для поиска телефонных номеров в зависимости от страны.

    :param lang: строка, представляющая код страны (ru, usa, bel, ch)
    :return: регулярное выражение для поиска номеров
    """
    patterns = {
        'ru': r'\+7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}',  # Россия
        'usa': r'\+1[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}',  # США
        'bel': r'\+375[\s-]?\(?\d{2}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}',  # Беларусь
        'ch': r'\+86[\s-]?\d{3}[\s-]?\d{4}[\s-]?\d{4}'  # Китай
    }
    return patterns.get(lang, None)

def find_phone_numbers(file_path, lang):
    """
    Функция для поиска уникальных телефонных номеров в текстовом файле.

    :param file_path: путь к текстовому файлу
    :param lang: код страны (ru, usa, bel, ch)
    :return: список уникальных номеров телефонов
    """
    try:
        # Получение регулярного выражения для выбранной страны
        phone_pattern = get_phone_pattern(lang)
        if not phone_pattern:
            print(f"Формат страны '{lang}' не поддерживается.")
            return []

        # Чтение содержимого файла
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Поиск номеров телефонов
        phones = re.findall(phone_pattern, text)

        # Возвращаем уникальные номера
        unique_phones = list(set(phones))
        return unique_phones

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []

# Пример использования
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Поиск номеров телефонов.")
    parser.add_argument("--file", required=True, help="Путь к текстовому файлу")
    parser.add_argument("--lang", required=True, help="Код страны (ru, usa, bel, ch)")

    args = parser.parse_args()
    result = find_phone_numbers(args.file, args.lang)

    if result:
        print("Найденные уникальные номера телефонов:")
        for phone in result:
            print(phone)
    else:
        print("Телефонных номеров не найдено.")
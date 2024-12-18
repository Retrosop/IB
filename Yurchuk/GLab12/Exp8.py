import re


def get_validation_pattern(country_code):
    """
    Возвращает регулярное выражение для проверки корректности номеров телефонов в зависимости от страны.

    :param country_code: строка, представляющая код страны (ru, ca, cz, fi)
    :return: регулярное выражение для проверки номера телефона
    """
    patterns = {
        'ru': r'\+7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}',  # Россия
        'ca': r'\+1[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}',  # Канада
        'cz': r'\+420[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3}',  # Чехия
        'fi': r'\+358[\s-]?\d{2,3}[\s-]?\d{3}[\s-]?\d{2,3}'  # Финляндия
    }
    return patterns.get(country_code, None)


def validate_phone_number(phone_number, country_code):
    """
    Проверяет корректность телефонного номера в зависимости от формата страны.

    :param phone_number: строка, представляющая телефонный номер
    :param country_code: код страны (ru, ca, cz, fi)
    :return: True, если номер корректен, иначе False
    """
    pattern = get_validation_pattern(country_code)
    if not pattern:
        raise ValueError(f"Формат страны '{country_code}' не поддерживается.")

    return bool(re.match(pattern, phone_number))


def validate_numbers_from_file(file_path, country_code):
    """
    Проверяет корректность всех телефонных номеров, перечисленных в текстовом файле.

    :param file_path: путь к текстовому файлу
    :param country_code: код страны (ru, ca, cz, fi)
    :return: список пар (номер телефона, результат проверки True/False)
    """
    try:
        # Чтение содержимого файла
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        results = []
        for line in lines:
            phone_number = line.strip()  # Удаление лишних пробелов
            if phone_number:
                is_valid = validate_phone_number(phone_number, country_code)
                results.append((phone_number, is_valid))

        return results

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []


# Пример использования
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Валидация номеров телефонов.")
    parser.add_argument("--file", required=True, help="Путь к текстовому файлу с номерами телефонов")
    parser.add_argument("--lang", required=True, help="Код страны (ru, ca, cz, fi)")

    args = parser.parse_args()
    validation_results = validate_numbers_from_file(args.file, args.lang)

    if validation_results:
        print("Результаты проверки номеров телефонов:")
        for number, result in validation_results:
            print(f"{number}: {'Корректный' if result else 'Некорректный'}")
    else:
        print("В файле нет номеров телефонов или файл отсутствует.")
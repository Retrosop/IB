def get_unique_lines(text, sort=False):
    # Разбиваем текст на строки
    lines = text.splitlines()

    # Получаем уникальные строки с помощью множества
    unique_lines = set(lines)

    # Преобразуем множество обратно в список для дальнейшей работы
    unique_lines_list = list(unique_lines)

    # Словарь для сопоставления строк с числовыми значениями
    number_words = {
        'один': 1,
        'два': 2,
        'три': 3,
        # Добавьте другие числа по необходимости
    }

    # Сортируем, если это необходимо
    if sort:
        unique_lines_list.sort(key=lambda x: number_words.get(x.split()[-1], float('inf')))

    return unique_lines_list


# Пример использования
input_text = """строка один
строка три
строка два
строка один
строка два"""

# Получение уникальных строк без сортировки
unique_lines = get_unique_lines(input_text)
print("Уникальные строки без сортировки:")
print(unique_lines)

# Получение уникальных строк с сортировкой
unique_sorted_lines = get_unique_lines(input_text, sort=True)
print("\nУникальные строки с сортировкой:")
print(unique_sorted_lines)

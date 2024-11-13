import os

# Функция для поиска файлов, содержащих указанный текст
def search_files(directory, text):
    found_files = []  # Список для хранения найденных файлов
    ignore_case = True  # Игнорируем регистр
    recursive = True  # Включаем рекурсивный поиск
    max_depth = float('inf')  # Устанавливаем неограниченную глубину

    # Вложенная функция для рекурсивного поиска в директории
    def search_in_directory(current_directory, current_depth):
        if current_depth > max_depth:  # Проверяем, не превышена ли максимальная глубина
            return
        try:
            for entry in os.listdir(current_directory):  # Перебираем все элементы в текущей директории
                path = os.path.join(current_directory, entry)  # Формируем полный путь к элементу
                if os.path.isdir(path):  # Если элемент - директория
                    if recursive:  # Если включен рекурсивный поиск
                        search_in_directory(path, current_depth + 1)  # Рекурсивно ищем в поддиректории
                else:  # Если элемент - файл
                    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                        file_content = file.read()  # Читаем содержимое файла
                        # Проверяем, содержится ли текст в файле (с учетом регистра или без)
                        if (ignore_case and text in file_content.lower()) or (not ignore_case and text in file_content):
                            found_files.append(path)  # Добавляем файл в список найденных
        except PermissionError:
            pass  # Игнорируем ошибки доступа к файлам

    search_in_directory(directory, 0)  # Запускаем поиск в указанной директории
    return found_files  # Возвращаем список найденных файлов

if __name__ == "__main__":
    # Ввод текста и директории с клавиатуры
    text = input("Введите текст для поиска: ")  # Запрашиваем текст для поиска
    directory = input("Введите путь к директории: ")  # Запрашиваем путь к директории

    # Выполняем поиск
    results = search_files(directory, text)
    if results:  # Если найдены файлы
        print("Найденные файлы:")  # Выводим заголовок
        for result in results:  # Перебираем найденные файлы
            print(result)  # Выводим каждый найденный файл
    else:  # Если файлы не найдены
        print("Файлы не найдены.")  # Выводим сообщение о том, что файлы не найдены
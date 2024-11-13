import os

def find_files(directory, size, greater_than, less_than, recursive):
    found_files = []

    # Вложенная функция для рекурсивного поиска
    def search_in_directory(current_directory):
        for entry in os.listdir(current_directory):
            path = os.path.join(current_directory, entry)
            if os.path.isdir(path) and recursive:
                search_in_directory(path)  # Рекурсивный вызов для поддиректорий
            elif os.path.isfile(path):
                file_size = os.path.getsize(path)
                if (greater_than and file_size > size) or (less_than and file_size < size):
                    found_files.append((path, file_size))

    search_in_directory(directory)  # Запускаем поиск в указанной директории
    return found_files

def main():
    # Ввод параметров с клавиатуры
    size = int(input("Введите размер в байтах для поиска: "))  # Запрашиваем размер
    directory = input("Введите путь до директории: ")  # Запрашиваем путь к директории

    # Задаем фиксированные параметры поиска
    recursive = True  # Всегда включаем рекурсивный поиск
    greater_than = True  # Искать файлы с большим размером
    less_than = False  # Не искать файлы с меньшим размером

    # Выполнение поиска
    results = find_files(directory, size, greater_than, less_than, recursive)

    # Вывод результатов
    if results:
        print("Найденные файлы:")
        for file_path, file_size in results:
            print(f"{file_path}: {file_size} байт")
    else:
        print("Файлы не найдены.")

if __name__ == "__main__":
    main()
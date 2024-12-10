import os
import datetime


def search_files_by_modification_date(directory, ref_date, recursive=True, older=False, newer=False, sort=False):
    matched_files = []

    def is_older(file_date, ref_date):
        return file_date < ref_date

    def is_newer(file_date, ref_date):
        return file_date > ref_date

    def search_directory(current_path):
        try:
            for entry in os.scandir(current_path):
                if entry.is_file():
                    file_mod_time = datetime.datetime.fromtimestamp(entry.stat().st_mtime)

                    if (older and is_older(file_mod_time, ref_date)) or (newer and is_newer(file_mod_time, ref_date)):
                        matched_files.append((entry.path, file_mod_time))

                elif entry.is_dir() and recursive:
                    search_directory(entry.path)
        except PermissionError:
            print(f"Нет доступа к {current_path}")

    search_directory(directory)

    if sort:
        matched_files.sort(key=lambda x: x[1])  # Сортировка по дате модификации

    return matched_files


# Ввод данных для поиска
directory_path = input("Введите путь до директории: ")
date_input = input("Введите дату (в формате ГГГГ-ММ-ДД): ")
ref_date = datetime.datetime.strptime(date_input, '%Y-%m-%d')
older_than = input("Искать файлы старше указанной даты? (да/нет): ").strip().lower() == 'да'
newer_than = input("Искать файлы новее указанной даты? (да/нет): ").strip().lower() == 'да'
sort_files = input("Отсортировать файлы по дате модификации? (да/нет): ").strip().lower() == 'да'

# Поиск файлов
files_found = search_files_by_modification_date(directory_path, ref_date, recursive=True, older=older_than,
                                                newer=newer_than, sort=sort_files)

# Вывод результатов
if files_found:
    print("Найденные файлы:")
    for file_path, mod_time in files_found:
        print(f"{file_path} - Дата модификации: {mod_time}")
else:
    print("Файлы с заданными критериями не найдены.")

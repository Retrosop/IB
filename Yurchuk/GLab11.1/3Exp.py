import os
from docx import Document

def contains_text(file_path, text, ignore_case):
    try:
        if file_path.endswith('.docx'):
            # Read .docx file
            doc = Document(file_path)
            content = '\n'.join([para.text for para in doc.paragraphs])
        else:
            # Read text file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

        if ignore_case:
            return text.lower() in content.lower()
        else:
            return text in content
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return False

def search_files_with_text(directory, text, recursive=True, max_depth=None, ignore_case=False):
    results = []

    def search_in_directory(current_dir, current_depth):
        if max_depth is not None and current_depth > max_depth:
            return

        try:
            for entry in os.scandir(current_dir):
                if entry.is_file() and contains_text(entry.path, text, ignore_case):
                    results.append(entry.path)
                elif entry.is_dir() and recursive:
                    search_in_directory(entry.path, current_depth + 1)
        except PermissionError:
            print(f"Нет доступа к {current_dir}")

    search_in_directory(directory, 0)
    return results

# Пример использования
search_text = input("Введите текст для поиска: ")
directory_path = input("Введите путь до директории: ")
recursive_search = input("Рекурсивный поиск? (да/нет): ").strip().lower() == 'да'
max_search_depth = input("Введите максимальную глубину поиска (или оставьте пустым для неограниченного поиска): ")
max_search_depth = int(max_search_depth) if max_search_depth else None
ignore_case = input("Игнорировать регистр символов? (да/нет): ").strip().lower() == 'да'

files_found = search_files_with_text(directory_path, search_text, recursive=recursive_search,
                                     max_depth=max_search_depth, ignore_case=ignore_case)

if files_found:
    print("Файлы, содержащие указанный текст:")
    for file in files_found:
        print(file)
else:
    print("Файлы с указанным текстом не найдены.")

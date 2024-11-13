import re

def find_unique_links(file_path):
    # Чтение HTML-файла
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Регулярное выражение для поиска ссылок
    pattern = r'href=["\'](http[s]?://[^"\']+)["\']'
    links = set(re.findall(pattern, html_content))
    
    return list(links)

# Запрос пути к файлу у пользователя
file_path = input("Введите путь к вашему HTML-файлу: ")  # Ввод с клавиатуры
unique_links = find_unique_links(file_path)

# Вывод уникальных ссылок в заданном формате
if unique_links:
    print("Найденные уникальные ссылки:")
    for link in unique_links:
        # Форматирование ссылки в нужный HTML-формат
        print(f' {link} ')
else:
    print("Ссылки не найдены.")
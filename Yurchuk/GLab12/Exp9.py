import re


def find_ipv4_addresses(file_path):
    """
    Находит все уникальные IPv4 адреса в указанном текстовом файле.

    :param file_path: путь к текстовому файлу
    :return: список уникальных IPv4 адресов
    """
    # Регулярное выражение для IPv4 адресов
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

    try:
        # Чтение содержимого файла
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Поиск всех IPv4 адресов
        ipv4_addresses = re.findall(ipv4_pattern, text)

        # Удаляем дубликаты, возвращаем как список
        return list(set(ipv4_addresses))

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []


# Пример использования
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Поиск уникальных IPv4 адресов в тексте.")
    parser.add_argument("--file", required=True, help="Путь к текстовому файлу для анализа.")

    args = parser.parse_args()
    ipv4_addresses = find_ipv4_addresses(args.file)

    if ipv4_addresses:
        print("Найденные уникальные IPv4 адреса:")
        for ip in ipv4_addresses:
            print(ip)
    else:
        print("IPv4 адреса не найдены или файл пуст.")
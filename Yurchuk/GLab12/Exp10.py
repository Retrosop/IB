import re

def is_valid_ipv4_address(ip_address):
    """
    Проверяет, является ли переданная строка корректным IPv4 адресом.

    :param ip_address: строка, представляющая IPv4 адрес
    :return: True, если строка является корректным IPv4 адресом, иначе False
    """
    # Регулярное выражение для IPv4 адресов
    ipv4_pattern = r'^\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b$'

    # Проверка на соответствие формату
    if not re.match(ipv4_pattern, ip_address):
        return False

    # Проверка каждого октета на диапазон 0-255
    octets = ip_address.split('.')
    for octet in octets:
        if not (0 <= int(octet) <= 255):
            return False

    return True

def read_addresses_from_file(file_path):
    """
    Считывает IP адреса из файла и проверяет их корректность.

    :param file_path: путь к текстовому файлу с IP адресами
    :return: список кортежей (IP адрес, True/False)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        results = []
        for line in lines:
            ip_address = line.strip()  # Удалить пробелы и символы новой строки
            if ip_address:
                is_valid = is_valid_ipv4_address(ip_address)
                results.append((ip_address, is_valid))

        return results

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []

# Пример использования
if __name__ == "__main__":
    file_path = "D:/Python_progects/GLab12/IPv4.1.txt"
    validation_results = read_addresses_from_file(file_path)

    if validation_results:
        print("Результаты проверки IPv4 адресов:")
        for address, is_valid in validation_results:
            print(f"{address}: {'Корректный' if is_valid else 'Некорректный'}")
    else:
        print("IPv4 адреса не найдены или файл отсутствует.")

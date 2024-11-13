import re

def find_unique_ipv4_addresses(file_path):
    # Регулярное выражение для поиска корректных IPv4 адресов
    ipv4_pattern = re.compile(
        r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    )
    
    unique_ipv4_addresses = set()  # Используем множество для хранения уникальных IPv4 адресов

    # Чтение текстового файла
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Находим все IPv4 адреса в строке
            ipv4_addresses = ipv4_pattern.findall(line)
            for ip in ipv4_addresses:
                # Проверяем, что каждый октет находится в диапазоне от 0 до 255
                octets = ip.split('.')
                if all(0 <= int(octet) <= 255 for octet in octets):
                    unique_ipv4_addresses.add(ip)  # Добавляем найденные адреса в множество

    return list(unique_ipv4_addresses)  # Преобразуем множество в список для возврата

# Пример использования
file_path = input("Введите путь к текстовому файлу: ")
unique_ipv4_addresses = find_unique_ipv4_addresses(file_path)

# Вывод уникальных IPv4 адресов
if unique_ipv4_addresses:
    print("Найденные уникальные IPv4 адреса:")
    for ip in unique_ipv4_addresses:
        print(ip)
else:
    print("IPv4 адреса не найдены.")
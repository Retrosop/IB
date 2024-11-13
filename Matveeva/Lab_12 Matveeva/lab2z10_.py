import re

def is_valid_ipv4(ip):
    # Регулярное выражение для проверки корректности IPv4 адреса
    ipv4_pattern = re.compile(
        r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    )
    
    # Проверяем, соответствует ли строка шаблону
    if ipv4_pattern.match(ip):
        # Разбиваем адрес на октеты
        octets = ip.split('.')
        # Проверяем, что каждый октет находится в диапазоне от 0 до 255
        return all(0 <= int(octet) <= 255 for octet in octets)
    
    return False

# Пример использования
ip_input = input("Введите IPv4 адрес для проверки: ")
if is_valid_ipv4(ip_input):
    print("True")
else:
    print("False")
import os
import numpy as np

def lcg(seed, a=1664525, c=1013904223, m=2**32):
    """Генератор линейного конгруэнтного метода (LCG)"""
    while True:
        seed = (a * seed + c) % m
        yield seed & 0xFF  # Возвращаем младший байт

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(data)

def xor_encrypt(text, key_stream):
    return ''.join(chr(ord(c) ^ next(key_stream)) for c in text)

def main():
    base_path = r"C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python38"
    source_file = os.path.join(base_path, "Source.txt")
    coded_file = os.path.join(base_path, "Coded.txt")
    decoded_file = os.path.join(base_path, "DeCoded.txt")
    
    seed = 123456789  # Начальное значение генератора
    key_stream = lcg(seed)
    
    # Читаем исходный текст
    source_text = read_file(source_file)
    
    # Шифруем
    encrypted_text = xor_encrypt(source_text, key_stream)
    write_file(coded_file, encrypted_text)
    
    # Дешифруем
    key_stream = lcg(seed)  # Перезапускаем генератор с тем же seed
    decrypted_text = xor_encrypt(encrypted_text, key_stream)
    write_file(decoded_file, decrypted_text)
    
    print("Шифрование и расшифрование завершены.")

if __name__ == "__main__":
    main()

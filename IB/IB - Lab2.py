import string
import os

def create_polybius_square():
    """Создает квадрат Полибия для символов английского алфавита и цифр."""
    alphabet = string.ascii_lowercase + string.digits
    size = 6  # 6x6 квадрат
    square = {}
    index = 0
    
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            if index < len(alphabet):
                square[alphabet[index]] = f"{row}{col}"
                index += 1
    
    return square

def encrypt_polybius(text, square):
    """Шифрует текст с использованием квадрата Полибия."""
    text = text.lower()
    encrypted = ''.join(square[char] if char in square else char for char in text)
    return encrypted

def decrypt_polybius(encrypted_text, square):
    """Дешифрует текст, зашифрованный квадратом Полибия."""
    reversed_square = {v: k for k, v in square.items()}
    decrypted = ''
    i = 0
    while i < len(encrypted_text):
        if encrypted_text[i].isdigit() and i + 1 < len(encrypted_text) and encrypted_text[i + 1].isdigit():
            decrypted += reversed_square.get(encrypted_text[i:i + 2], '?')
            i += 2
        else:
            decrypted += encrypted_text[i]
            i += 1
    return decrypted

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def process_files(base_path):
    square = create_polybius_square()
    source_path = os.path.join(base_path, "Source.txt")
    coded_path = os.path.join(base_path, "Coded.txt")
    decoded_path = os.path.join(base_path, "DeCoded.txt")
    
    # Читаем исходный текст
    plaintext = read_file(source_path)
    
    # Шифруем текст
    encrypted_text = encrypt_polybius(plaintext, square)
    write_file(coded_path, encrypted_text)
    
    # Дешифруем текст
    decrypted_text = decrypt_polybius(encrypted_text, square)
    write_file(decoded_path, decrypted_text)
    
    print("Шифрование и дешифрование завершено. Файлы сохранены.")

# Укажите путь к папке, где находятся файлы
base_path = r"C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python38"
process_files(base_path)

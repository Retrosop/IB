import random

def generate_key(length):
    """Генерирует случайный ключ заданной длины."""
    return [random.randint(0, 10) for _ in range(length)]

def vernam_cipher(message, key):
    """Шифрует сообщение с помощью шифра Вернама."""
    encrypted_message = []
    for i in range(len(message)):
        # Применяем XOR между символом сообщения и соответствующим битом ключа
        encrypted_bit = ord(message[i]) ^ key[i % len(key)]
        encrypted_message.append(encrypted_bit)
    return encrypted_message

# Ввод сообщения с клавиатуры
message = input("Введите сообщение для шифрования: ")
key_length = 5
key = generate_key(key_length)
encrypted = vernam_cipher(message, key)

print("Сообщение:", message)
print("Ключ:", key)
print("Зашифрованное сообщение:", encrypted)
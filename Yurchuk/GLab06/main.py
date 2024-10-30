import random

#Генерирует случайный ключ заданной длины
def generate_key(length):
    return [random.randint(0, 10) for _ in range(length)]

#Шифрует сообщение с помощью шифра Вернама
def vernam_cipher(message, key):
    encrypted_message = []
    for i in range(len(message)):
        # Применяем XOR между символом сообщения и соответствующим битом ключа
        encrypted_bit = ord(message[i]) ^ key[i % len(key)]
        encrypted_message.append(encrypted_bit)
    return encrypted_message

#Добавляет пароль в начало зашифрованного сообщения
def add_password_to_encrypted(encrypted_message, password):
    password_bits = [ord(char) for char in password]
    return password_bits + encrypted_message

# Ввод пароля с клавиатуры
correct_password = input("Придумайте пароль для шифрования: ")

# Ввод сообщения с клавиатуры
message = input("Введите сообщение для шифрования: ")
message_with_password = correct_password + message

key_length = 5
key = generate_key(key_length)
encrypted = vernam_cipher(message_with_password, key)
encrypted_with_password = add_password_to_encrypted(encrypted, correct_password)

# Вывод зашифрованного пароля и сообщения
encrypted_password = [ord(char) for char in correct_password]
print("Зашифрованный пароль:", encrypted_password)
print("Зашифрованное сообщение:", encrypted)

# Вывод зашифрованного пароля и сообщения вместе
print("Зашифрованное сообщение с паролем:", encrypted_with_password)

# Запуск расшифровки
input_password = input("Введите пароль для расшифровки: ")

if input_password == correct_password:
    print("Пароль верен!")
else:
    print("Неверный пароль!")
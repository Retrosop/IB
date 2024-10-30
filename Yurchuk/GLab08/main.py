# Определяем параметры RSA
P = 62
Q = 53
N = P * Q  # Модуль
phi_N = (P - 1) * (Q - 1)  # Функция Эйлера
e = 17
d = 2753

# Функция для шифрования
def encrypt(message):
    encrypted_message = []
    for char in message:
        # Преобразуем символ в число (А=1, Б=2, ..., Я=33)
        m = ord(char) - ord('А') + 1  # Для русского алфавита
        c = pow(m, e, N)  # Шифруем
        encrypted_message.append(c)
    return encrypted_message

# Функция для дешифрования
def decrypt(encrypted_message):
    decrypted_message = ''
    for c in encrypted_message:
        m = pow(c, d, N)  # Дешифруем
        decrypted_message += chr(m + ord('А') - 1)  # Преобразуем обратно в символ
    return decrypted_message

# Основная программа
if __name__ == "__main__":
    # Вводим сообщение с клавиатуры
    original_message = input("Введите сообщение (только русские буквы): ")

    # Шифруем сообщение
    encrypted_message = encrypt(original_message)

    # Дешифруем сообщение
    decrypted_message = decrypt(encrypted_message)

    # Сохраняем результаты в файлы
    with open("original_message.txt", "w", encoding='utf-8') as f:
        f.write(original_message)

    with open("encrypted_message.txt", "w", encoding='utf-8') as f:
        f.write(' '.join(map(str, encrypted_message)))

    with open("decrypted_message.txt", "w", encoding='utf-8') as f:
        f.write(decrypted_message)

    print("Шифрование и дешифрование завершены. Результаты сохранены в файлы.")
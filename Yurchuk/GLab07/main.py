import os


# Функция для возведения в степень по модулю
def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:  # Если exponent нечетный
            result = (result * base) % modulus
        exponent = exponent >> 1  # Делим exponent на 2
        base = (base * base) % modulus
    return result


# Генерация ключей
def generate_keys(p, g, x):
    y = modular_exponentiation(g, x, p)  # Открытый ключ
    return y


# Шифрование сообщения
def encrypt_message(message, p, g, y):
    k = 3  # Случайное число (должно быть выбрано случайно)
    c1 = modular_exponentiation(g, k, p)
    c2 = (message * modular_exponentiation(y, k, p)) % p
    return c1, c2


# Восстановление сообщения
def decrypt_message(c1, c2, x, p):
    s = modular_exponentiation(c1, x, p)  # Секретный ключ
    s_inv = pow(s, -1, p)  # Обратный элемент
    message = (c2 * s_inv) % p
    return message


# Основная функция
def main():
    # Параметры алгоритма
    p = 23  # Простое число
    g = 5  # Генератор
    x = 6  # Секретный ключ (должен быть случайным)

    # Исходное сообщение
    message = 656339  # Сообщение как число

    # Генерация открытого ключа
    y = generate_keys(p, g, x)

    # Шифрование
    c1, c2 = encrypt_message(message, p, g, y)

    # Восстановление сообщения
    decrypted_message = decrypt_message(c1, c2, x, p)

    # Сохранение в файлы
    with open('original_message.txt', 'w') as f:
        f.write(str(message))

    with open('encrypted_message.txt', 'w') as f:
        f.write(f"{c1}, {c2}")

    with open('decrypted_message.txt', 'w') as f:
        f.write(str(decrypted_message))

    print("Шифрование и восстановление завершены. Результаты сохранены в файлы.")


if __name__ == "__main__":
    main()
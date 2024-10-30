import math
import random


def gcd(m, n):
    # Функция для нахождения наибольшего общего делителя (НОД) двух чисел
    while m != 0 and n != 0:
        if m > n:
            m = m % n
        else:
            n = n % m
    return n if n != 0 else m


def is_prime(p):
    # Функция для проверки, является ли число простым
    if p <= 1:
        return False
    for k in range(2, int(math.sqrt(p)) + 1):
        if p % k == 0:
            return False
    return True


def next_prime(p):
    # Функция для нахождения следующего простого числа
    while not is_prime(p):
        p += 1
    return p


def power_mod(g, k, p):
    # Функция для вычисления g^k mod p
    return pow(g, k, p)


def elgamal_encrypt(p, g, a, message):
    # Генерация открытого ключа
    y = power_mod(g, a, p)
    encrypted_message = []

    for c in message:
        # Генерируем случайное число k
        k = random.randint(1, p - 2)

        # Находим взаимно простое число k с p-1
        while gcd(k, p - 1) != 1:
            k += 1

        # Вычисляем зашифрованные части сообщения
        y1 = chr(power_mod(g, k, p))
        key = power_mod(y, k, p)
        y2 = chr(ord(c) ^ key)
        encrypted_message.append((y1, y2))

    return encrypted_message


def elgamal_decrypt(p, a, encrypted_message):
    decrypted_message = []
    for y1, y2 in encrypted_message:
        # Восстанавливаем исходное сообщение
        c = chr((power_mod(ord(y1), a, p) ^ ord(y2)))
        decrypted_message.append(c)
    return ''.join(decrypted_message)


def main():
    # Задаем параметры шифрования
    p = 11
    g = 9
    a = 5

    # Находим следующее простое число
    p = next_prime(p)

    # Вводим сообщение с клавиатуры
    message = input("Введите сообщение для шифрования: ")

    # Шифруем сообщение
    encrypted_message = elgamal_encrypt(p, g, a, message)
    print("Зашифрованное сообщение:", encrypted_message)

    # Дешифруем сообщение
    decrypted_message = elgamal_decrypt(p, a, encrypted_message)
    print("Расшифрованное сообщение:", decrypted_message)


if __name__ == '__main__':
    main()

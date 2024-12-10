import random


def is_prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        # Выбираем случайное число a в диапазоне [2, n-2]
        a = random.randint(2, n - 2)
        # Проверяем условие a^(n-1) ≡ 1 (mod n)
        if pow(a, n - 1, n) != 1:
            return False

    return True


# Пример использования
try:
    n = int(input("Введите число для проверки на простоту: "))
    if is_prime_fermat(n):
        print(f"Число {n} вероятно простое.")
    else:
        print(f"Число {n} составное.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")

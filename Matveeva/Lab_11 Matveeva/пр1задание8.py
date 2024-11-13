import random

def is_prime_fermat(n, k=5):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    # Тест Ферма
    for _ in range(k):
        a = random.randint(2, n - 2)  # Случайное число от 2 до n-2
        if pow(a, n - 1, n) != 1:  # Проверка условия Ферма
            return False
    return True

def main():
    try:
        n = int(input("Введите целое число для проверки на простоту: "))  # Запрашиваем число
        result = is_prime_fermat(n)  # Выполняем тест Ферма
        print(f"Число {n} является простым: {result}.")
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()
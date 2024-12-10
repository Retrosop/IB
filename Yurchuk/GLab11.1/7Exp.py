def fibonacci(n):
    if n <= 0:
        raise ValueError("Порядковый номер должен быть положительным целым числом.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Пример использования
try:
    n = int(input("Введите порядковый номер числа Фибоначчи: "))
    fib_number = fibonacci(n)
    print(f"Число Фибоначчи с порядковым номером {n} равно {fib_number}.")
except ValueError as e:
    print(e)

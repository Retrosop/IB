def fibonacci(n):
    if n <= 0:
        return "Порядковый номер должен быть положительным целым числом."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def main():
    try:
        n = int(input("Введите порядковый номер числа Фибоначчи: "))  # Запрашиваем порядковый номер
        result = fibonacci(n)  # Вычисляем число Фибоначчи
        print(f"Число Фибоначчи под номером {n} равно {result}.")
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()
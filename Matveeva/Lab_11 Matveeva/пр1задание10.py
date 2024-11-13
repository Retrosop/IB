def gcd(a, b):
    """Функция для вычисления наибольшего общего делителя (НОД)"""
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    """Функция для вычисления значения функции Эйлера φ(n)"""
    if n < 1:
        raise ValueError("Введите целое число больше 0.")
    
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:  # Проверка, является ли i взаимно простым с n
            count += 1
    return count

def main():
    try:
        n = int(input("Введите целое число для вычисления функции Эйлера: "))  # Запрашиваем число
        result = euler_totient(n)  # Вычисляем значение функции Эйлера
        print(f"Значение функции Эйлера φ({n}) равно {result}.")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
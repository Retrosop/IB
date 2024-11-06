def multiply(x, y):
    """Умножение в конечном поле с модулем 0x10001, с учетом замены 0 на 0x10000"""
    if x == 0:
        x = 0x10000
    if y == 0:
        y = 0x10000
    result = (x * y) % 0x10001
    return 0 if result == 0x10000 else result

def add(x, y):
    """Сложение по модулю 0x10000 (16-битное сложение)"""
    return (x + y) % 0x10000

def xor(x, y):
    """Побитовое исключающее ИЛИ (XOR)"""
    return x ^ y

# Основные операции раунда 10-14
def idea_round_operations(x1, x2, x3, x4, subkeys):
    """
    Выполняет операции 10-14 для одного раунда IDEA
    :param x1, x2, x3, x4: 16-битные блоки данных
    :param subkeys: 6 субключей для текущего раунда
    :return: обновленные x1, x2, x3, x4
    """

    # Шаг 10: Умножить x1 и subkey[0]
    x1 = multiply(x1, subkeys[0])

    # Шаг 11: Сложить x2 и subkey[1]
    x2 = add(x2, subkeys[1])

    # Шаг 12: Сложить x3 и subkey[2]
    x3 = add(x3, subkeys[2])

    # Шаг 13: Умножить x4 и subkey[3]
    x4 = multiply(x4, subkeys[3])

    # Шаг 14: Выполнить XOR для x1 и x3, x2 и x4
    t1 = xor(x1, x3)
    t2 = xor(x2, x4)

    return x1, x2, x3, x4, t1, t2

# Пример вызова функций для одного раунда с тестовыми значениями
# Предположим, что x1, x2, x3, x4 — это 16-битные части входных данных, и subkeys — 6 субключей
x1, x2, x3, x4 = 0x1234, 0x5678, 0x9abc, 0xdef0
subkeys = [0x1111, 0x2222, 0x3333, 0x4444, 0x5555, 0x6666]

# Выполнение операций раунда
x1, x2, x3, x4, t1, t2 = idea_round_operations(x1, x2, x3, x4, subkeys)
print(f"Результаты операций: x1={x1:04x}, x2={x2:04x}, x3={x3:04x}, x4={x4:04x}, t1={t1:04x}, t2={t2:04x}")
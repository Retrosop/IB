# Создание алфавита
russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  # Русский алфавит

# Ввод текста для шифрования
text = input("Введите текст для шифрования (используйте только русские буквы): ")

# Вычисление количества символов в тексте
text_length = len(text)
print("Количество символов в введенном тексте:", text_length)

# Определение размера магического квадрата на основе количества символов
if text_length <= 9:
    n = 3
elif 10 <= text_length <= 16:
    n = 4
elif 17 <= text_length <= 25:
    n = 5
else:
    n = 6

# Нумерация символов введенного текста
numbered_text = []
for char in text.upper():
    if char in russian_alphabet:
        index = russian_alphabet.index(char) + 1
        numbered_text.append(index)

def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    num: int = 1
    i, j = 0, n // 2  # Начальная позиция (первая строка, центральный столбец)

    while num <= n ** 2:
        magic_square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n  # Переход к следующей позиции

        if magic_square[new_i][new_j]:  # Если ячейка занята
            i += 1  # Переход вниз
        else:
            i, j = new_i, new_j  # Переход к новой позиции

    return magic_square

def print_magic_square(square):
    for row in square:
        print(" ".join(f"{num:2}" for num in row))

def encrypt_text(text):
    encrypted_text = []
    for char in text.upper():
        if char in russian_alphabet:
            index = russian_alphabet.index(char) + 1  # Номер символа
            encrypted_text.append(index)
    return encrypted_text

def decrypt_text(encrypted_text):
    decrypted_text = []
    for num in encrypted_text:
        if num > 0 and num <= len(russian_alphabet):
            decrypted_text.append(russian_alphabet[num - 1])  # Получение символа по номеру
    return ''.join(decrypted_text)

# Генерация магического квадрата
magic_square = generate_magic_square(n)

print("\nМагический квадрат (перед заполнением):")
print_magic_square(magic_square)

# Заполнение магического квадрата номерами символов из текста
index = 0
for i in range(n):
    for j in range(n):
        if index < len(numbered_text):
            magic_square[i][j] = numbered_text[index]
            index += 1
        else:
            magic_square[i][j] = 0  # Заполняем нулями, если символов не хватает

print("\nЗаполненный магический квадрат:")
print_magic_square(magic_square)

# Шифрование текста
encrypted_text = encrypt_text(text)
print("Зашифрованный текст (номера символов):", encrypted_text)

# Дешифрование текста
decrypted_text = decrypt_text(encrypted_text)
print("Дешифрованный текст:", decrypted_text)
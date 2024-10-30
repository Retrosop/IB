def rnd_init():
    # Инициализация начального значения генератора
    return 502

def rnd(a, m, y):
    # Генерация следующего значения псевдослучайной последовательности
    return (a * y) % m

def process_file(input_file, output_file, a, m, initial_y, mode='encrypt'):
    # Функция для обработки файла: шифрование или расшифрование
    y = initial_y
    block_size = 8  # Размер блока в байтах

    # Открываем входной файл для чтения в бинарном режиме и выходной файл для записи
    with open(input_file, 'rb') as fin, open(output_file, 'wb') as fout:
        while True:
            gamma = bytearray(block_size)  # Создаем массив для гаммы
            for i in range(block_size):
                y = rnd(a, m, y)  # Генерируем следующее значение гаммы
                gamma[i] = y % 256  # Преобразуем в байт

            text_block = fin.read(block_size)  # Читаем блок текста
            if not text_block:
                break  # Прерываем цикл, если достигнут конец файла

            processed_block = bytearray(len(text_block))
            for j in range(len(text_block)):
                # Применяем XOR для шифрования или расшифрования
                processed_block[j] = text_block[j] ^ gamma[j]

            fout.write(processed_block)  # Записываем обработанный блок в выходной файл


def main():
    # Очищаем файлы перед началом работы
    open('Source.txt', 'w').close()
    open('Coded.txt', 'w').close()
    open('DeCoded.txt', 'w').close()

    # Ввод текста с клавиатуры и запись в файл Source.txt
    input_text = input("Введите текст для шифровки: ")
    with open('Source.txt', 'w', encoding='utf-8') as f:
        f.write(input_text)

    # Параметры генератора
    a = 3
    m = 4096
    initial_y = rnd_init()

    # Шифрование исходного текста
    process_file('Source.txt', 'Coded.txt', a, m, initial_y, mode='encrypt')

    # Расшифрование текста
    initial_y = rnd_init()  # Сброс начального значения генератора
    process_file('Coded.txt', 'DeCoded.txt', a, m, initial_y, mode='decrypt')

    print("Шифрование и расшифрование завершено. Проверьте файлы Coded.txt и DeCoded.txt.")


if __name__ == "__main__":
    main()
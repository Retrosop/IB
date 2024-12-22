import struct

def parse_elf_header(filename):
    with open(filename, 'rb') as f:
        # Чтение ELF-заголовка (первые 52 байта для 32-битного ELF, 64 байта для 64-битного)
        elf_header = f.read(64)

        # Проверка сигнатуры ELF
        if elf_header[:4] != b'\x7fELF':
            raise ValueError("Файл не является ELF-файлом")

        # Определение разрядности (32-битный или 64-битный)
        ei_class = elf_header[4]
        if ei_class == 1:
            is_32bit = True
        elif ei_class == 2:
            is_32bit = False
        else:
            raise ValueError("Неизвестная разрядность ELF-файла")

        # Распаковка полей заголовка
        if is_32bit:
            # 32-битный ELF
            e_type, e_machine, e_version, e_entry, e_phoff, e_shoff = struct.unpack('<HHIIIII', elf_header[16:40])
        else:
            # 64-битный ELF
            e_type, e_machine, e_version, e_entry, e_phoff, e_shoff = struct.unpack('<HHIQQQ', elf_header[16:48])

        # Определение типа файла
        if e_type == 1:
            file_type = "RELOCATABLE"
        elif e_type == 2:
            file_type = "EXECUTABLE"
        elif e_type == 3:
            file_type = "DYNAMIC"
        elif e_type == 4:
            file_type = "CORE"
        else:
            file_type = "UNKNOWN"

        # Определение разрядности
        if is_32bit:
            bitness = "32-bit"
        else:
            bitness = "64-bit"

        # Вывод результатов
        print(f"Тип файла: {file_type}")
        print(f"Разрядность: {bitness}")
        print(f"Виртуальный адрес точки входа: {e_entry}")
        print(f"Смещение таблицы заголовков сегментов: {e_phoff}")
        print(f"Смещение таблицы заголовков секций: {e_shoff}")

# Пример использования
parse_elf_header("D:\Python_progects\Glab13\Lab01.elf")
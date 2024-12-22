import struct

# Определяем необходимые константы
MH_MAGIC_64 = 0xFEEDFACF
CPU_TYPE_X86_64 = 0x01000007
CPU_SUBTYPE_X86_64_ALL = 0x00000003
MH_EXECUTE = 0x2
LC_SEGMENT_64 = 0x19


def create_test_macho(file_path):
    # Открываем файл для записи в бинарном режиме
    with open(file_path, "wb") as f:
        # Создаём заголовок Mach-O
        magic = MH_MAGIC_64
        cputype = CPU_TYPE_X86_64  # Тип процессора (x86_64)
        cpusubtype = CPU_SUBTYPE_X86_64_ALL  # Подтип процессора
        filetype = MH_EXECUTE  # Тип файла (исполняемый файл)
        ncmds = 1  # Количество команд загрузки (1 сегмент)
        sizeofcmds = 72  # Размер всех команд загрузки (размер сегмента)
        flags = 0  # Флаги

        # Пишем заголовок в файл
        try:
            header = struct.pack(
                "<IiiIIII",
                magic,
                cputype,
                cpusubtype,
                filetype,
                ncmds,
                sizeofcmds,
                flags,
            )
            f.write(header)
        except struct.error as e:
            print(f"Ошибка при упаковке заголовка: {e}")
            return

        # Добавляем минимальный сегмент LC_SEGMENT_64
        segname = b"__TEXT" + b"\x00" * (16 - len("__TEXT"))  # Имя сегмента
        vmaddr = 0x1000  # Виртуальный адрес
        vmsize = 0x1000  # Размер в памяти
        fileoff = 0  # Смещение в файле
        filesize = 0x1000  # Размер в файле
        maxprot = 0x7  # Максимальные права доступа
        initprot = 0x5  # Начальные права доступа
        nsects = 0  # Количество секций
        flags = 0  # Флаги

        # Команда LC_SEGMENT_64
        cmd = LC_SEGMENT_64
        cmdsize = 72  # Размер команды (без секций)

        # Проверяем диапазоны значений
        if not (0 <= cmdsize <= 0xFFFFFFFF):
            raise ValueError("cmdsize out of range")
        if not (0 <= vmaddr <= 0xFFFFFFFFFFFFFFFF):
            raise ValueError("vmaddr out of range")
        if not (0 <= vmsize <= 0xFFFFFFFFFFFFFFFF):
            raise ValueError("vmsize out of range")
        if not (0 <= fileoff <= 0xFFFFFFFF):
            raise ValueError("fileoff out of range")
        if not (0 <= filesize <= 0xFFFFFFFF):
            raise ValueError("filesize out of range")

        try:
            segment_command = struct.pack(
                "<II16sQQQQiiII",
                cmd,
                cmdsize,
                segname,
                vmaddr,
                vmsize,
                fileoff,
                filesize,
                maxprot,
                initprot,
                nsects,
                flags,
            )
            f.write(segment_command)
        except struct.error as e:
            print(f"Ошибка при упаковке команды сегмента: {e}")
            return

    print(f"Тестовый Mach-O файл создан: {file_path}")


# Использование функции
if __name__ == "__main__":
    output_file = "test.macho"
    create_test_macho(output_file)

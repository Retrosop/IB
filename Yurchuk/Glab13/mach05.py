import struct

def create_macho_file(filename):
    # Создание заголовка Mach-O (64-битный)
    macho_header = b''
    macho_header += struct.pack('<I', 0xfeedfacf)  # magic (64-битный Mach-O)
    macho_header += struct.pack('<i', 0x1000007)  # cputype (x86_64)
    macho_header += struct.pack('<i', 3)         # cpusubtype (CPU_SUBTYPE_X86_64_ALL)
    macho_header += struct.pack('<I', 2)         # filetype (EXECUTE)
    macho_header += struct.pack('<I', 2)         # ncmds (количество команд загрузчику)
    macho_header += struct.pack('<I', 24)        # sizeofcmds (размер команд загрузчику)
    macho_header += struct.pack('<I', 0x100)     # flags (TWOLEVEL)
    macho_header += struct.pack('<I', 0)         # reserved (только для 64-битного Mach-O)

    # Создание команд загрузчика
    load_commands = b''
    # Команда LC_SEGMENT_64
    load_commands += struct.pack('<I', 0x19)     # cmd (LC_SEGMENT_64)
    load_commands += struct.pack('<I', 72)       # cmdsize (размер команды)
    load_commands += b'__TEXT\x00'              # segname (имя сегмента)
    load_commands += struct.pack('<Q', 0)        # vmaddr (виртуальный адрес)
    load_commands += struct.pack('<Q', 0x1000)   # vmsize (размер сегмента)
    load_commands += struct.pack('<Q', 0)        # fileoff (смещение в файле)
    load_commands += struct.pack('<Q', 0x1000)   # filesize (размер в файле)
    load_commands += struct.pack('<I', 7)        # maxprot (максимальная защита)
    load_commands += struct.pack('<I', 5)        # initprot (начальная защита)
    load_commands += struct.pack('<I', 1)        # nsects (количество секций)
    load_commands += struct.pack('<I', 0)        # flags

    # Секция __text
    load_commands += b'__text\x00'              # sectname (имя секции)
    load_commands += b'__TEXT\x00'              # segname (имя сегмента)
    load_commands += struct.pack('<Q', 0)        # addr (адрес секции)
    load_commands += struct.pack('<Q', 0x1000)   # size (размер секции)
    load_commands += struct.pack('<I', 0)        # offset (смещение в файле)
    load_commands += struct.pack('<I', 2)        # align (выравнивание)
    load_commands += struct.pack('<I', 0)        # reloff (смещение перемещений)
    load_commands += struct.pack('<I', 0)        # nreloc (количество перемещений)
    load_commands += struct.pack('<I', 0)        # flags
    load_commands += struct.pack('<I', 0)        # reserved1
    load_commands += struct.pack('<I', 0)        # reserved2

    # Запись в файл
    with open(filename, 'wb') as f:
        f.write(macho_header)
        f.write(load_commands)

# Создание Mach-O-файла
create_macho_file("Lab05.macho")
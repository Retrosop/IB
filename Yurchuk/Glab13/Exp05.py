import struct

def parse_macho_header(filename):
    with open(filename, 'rb') as f:
        # Чтение заголовка Mach-O (первые 32 байта для 32-битного, 36 байт для 64-битного)
        header = f.read(32)

        # Распаковка полей заголовка
        magic, cputype, cpusubtype, filetype, ncmds, sizeofcmds, flags = struct.unpack('<IiiIIII', header[:28])

        # Определение разрядности
        if magic == 0xfeedface:
            bitness = "32-bit"
        elif magic == 0xfeedfacf:
            bitness = "64-bit"
        else:
            raise ValueError("Неизвестный тип Mach-O-файла")

        # Определение типа файла
        filetype_map = {
            1: "OBJECT",
            2: "EXECUTE",
            3: "FVMLIB",
            4: "CORE",
            5: "PRELOAD",
            6: "DYLIB",
            7: "DYLINKER",
            8: "BUNDLE",
            9: "DYLIB_STUB",
            10: "DSYM",
            11: "KEXT_BUNDLE"
        }
        file_type = filetype_map.get(filetype, "UNKNOWN")

        # Определение флагов
        flags_map = {
            0x1: "NOUNDEFS",
            0x2: "INCRLINK",
            0x4: "DYLDLINK",
            0x8: "BINDATLOAD",
            0x10: "PREBOUND",
            0x20: "SPLIT_SEGS",
            0x40: "LAZY_INIT",
            0x80: "TWOLEVEL",
            0x100: "FORCE_FLAT",
            0x200: "NOMULTIDEFS",
            0x400: "NOFIXPREBINDING",
            0x800: "PREBINDABLE",
            0x1000: "ALLMODSBOUND",
            0x2000: "SUBSECTIONS_VIA_SYMBOLS",
            0x4000: "CANONICAL",
            0x8000: "WEAK_DEFINES",
            0x10000: "BINDS_TO_WEAK",
            0x20000: "ALLOW_STACK_EXECUTION",
            0x40000: "ROOT_SAFE",
            0x80000: "SETUID_SAFE",
            0x100000: "NO_REEXPORTED_DYLIBS",
            0x200000: "PIE",
            0x400000: "DEAD_STRIPPABLE_DYLIB",
            0x800000: "HAS_TLV_DESCRIPTORS",
            0x1000000: "NO_HEAP_EXECUTION",
            0x2000000: "APP_EXTENSION_SAFE"
        }
        flags_list = []
        for flag, name in flags_map.items():
            if flags & flag:
                flags_list.append(name)

        # Вывод результатов
        print(f"Тип файла: {file_type}")
        print(f"Разрядность: {bitness}")
        print(f"Количество команд загрузчику: {ncmds}")
        print(f"Флаги: {', '.join(flags_list)}")

# Пример использования
parse_macho_header("Lab05.macho")
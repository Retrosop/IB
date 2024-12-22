from elftools.elf.elffile import ELFFile

def parse_elf_sections(file_path):
    try:
        # Открытие ELF-файла
        with open(file_path, 'rb') as file:
            elf = ELFFile(file)
            sections_info = []

            # Парсинг заголовков секций
            for section in elf.iter_sections():
                section_name = section.name
                section_type = section['sh_type']
                section_offset = section['sh_offset']
                section_address = section['sh_addr']

                # Добавление информации о секции в список
                sections_info.append({
                    "name": section_name,
                    "type": section_type,
                    "offset": section_offset,
                    "virtual_address": section_address
                })

        return sections_info

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    file_path = input("Введите путь к ELF-файлу: ")
    result = parse_elf_sections(file_path)

    if "error" in result:
        print(f"Ошибка: {result['error']}")
    else:
        for section in result:
            print(f"Секция: {section['name']}")
            print(f"  Тип: {section['type']}")
            print(f"  Смещение (офсет): {section['offset']}")
            print(f"  Виртуальный адрес: {section['virtual_address']}")
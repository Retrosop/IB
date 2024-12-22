import pefile

def parse_pe_sections(file_path):
    try:
        # Загружаем PE-файл
        pe = pefile.PE(file_path)

        # Список для хранения информации о секциях
        sections_info = []

        # Перебираем секции
        for section in pe.sections:
            section_info = {
                "name": section.Name.decode('utf-8').strip('\x00'),
                "offset": hex(section.PointerToRawData),
                "virtual_address": hex(section.VirtualAddress),
                "attributes": {
                    "characteristics": hex(section.Characteristics),
                    "size_of_raw_data": hex(section.SizeOfRawData),
                    "virtual_size": hex(section.Misc_VirtualSize),
                }
            }
            sections_info.append(section_info)

        return sections_info

    except Exception as e:
        return {"error": str(e)}

# Пример использования
if __name__ == "__main__":
    file_path = input("Введите путь к PE-файлу: ")
    result = parse_pe_sections(file_path)

    if "error" in result:
        print(f"Ошибка: {result['error']}")
    else:
        for section in result:
            print(f"Секция: {section['name']}")
            print(f"  Смещение (офсет): {section['offset']}")
            print(f"  Виртуальный адрес: {section['virtual_address']}")
            print(f"  Атрибуты: {section['attributes']}")
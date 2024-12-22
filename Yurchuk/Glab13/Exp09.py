import pefile
import datetime

def parse_pe_file(file_path):
    try:
        # Загружаем PE-файл
        pe = pefile.PE(file_path)

        # Получение информации
        file_type = "PE32" if pe.FILE_HEADER.Machine == 0x14c else "PE64"
        timestamp = datetime.datetime.utcfromtimestamp(pe.FILE_HEADER.TimeDateStamp)
        number_of_sections = pe.FILE_HEADER.NumberOfSections
        attributes = {
            "Characteristics": hex(pe.FILE_HEADER.Characteristics),
            "Machine": hex(pe.FILE_HEADER.Machine)
        }

        # Результат
        result = {
            "file_type": file_type,
            "timestamp": timestamp,
            "number_of_sections": number_of_sections,
            "attributes": attributes
        }

        return result

    except Exception as e:
        return {"error": str(e)}

# Пример использования
if __name__ == "__main__":
    file_path = input("Введите путь к PE-файлу: ")
    result = parse_pe_file(file_path)

    if "error" in result:
        print(f"Ошибка: {result['error']}")
    else:
        print(f"Тип файла: {result['file_type']}")
        print(f"Дата сборки: {result['timestamp']}")
        print(f"Количество секций: {result['number_of_sections']}")
        print(f"Атрибуты: {result['attributes']}")
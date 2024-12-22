from macholib.MachO import MachO


def parse_mach_o(file_path):
    try:
        # Открываем Mach-O файл
        macho = MachO(file_path)
        segment_info = []

        # Перебираем команды загрузки
        for header in macho.headers:
            for command in header.commands:
                cmd = command[0]
                print(f"Обрабатываем команду: {cmd.get_cmd_name()}")  # Отладочная информация
                if cmd.get_cmd_name() in ("LC_SEGMENT", "LC_SEGMENT_64"):
                    segment_name = cmd.segname.decode("utf-8").strip("\x00")
                    segment_offset = cmd.fileoff
                    segment_address = cmd.vmaddr

                    # Получаем список секций
                    sections = []
                    for section in cmd.sections:
                        sections.append(section.sectname.decode("utf-8").strip("\x00"))

                    # Добавляем информацию о сегменте
                    segment_info.append({
                        "name": segment_name,
                        "offset": segment_offset,
                        "virtual_address": segment_address,
                        "sections": sections
                    })

        return segment_info

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    file_path = "test.macho"  # Убедитесь, что файл создан
    result = parse_mach_o(file_path)

    if "error" in result:
        print(f"Ошибка: {result['error']}")
    else:
        for segment in result:
            print(f"Сегмент: {segment['name']}")
            print(f"Смещение (офсет): {segment['offset']}")
            print(f"Виртуальный адрес: {segment['virtual_address']}")
            print(f"Секции: {', '.join(segment['sections']) if segment['sections'] else 'Нет'}")

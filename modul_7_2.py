def custom_write(file_name, strings):
    strings_positions = {}
    f = open(file_name, 'w', encoding='utf-8')
    f.writelines(f"{item}\n" for item in strings)
    str_num = 0
    str_start_byte = f.seek(0)
    for string_ in strings:
        f.write(string_ + '\n')
        str_num += 1
        key = (str_num, str_start_byte)
        strings_positions[key] = string_
        str_start_byte = f.tell()
    f.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
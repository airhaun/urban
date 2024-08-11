def custom_write(file_name, strings):
    string_position = {}
    file = open('text.txt', 'a', encoding='utf-8')

    for index, string in enumerate(strings, start=1):
        start_position = file.tell()
        file.write(string + '\n')
        string_position[(index, start_position)] = string

    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
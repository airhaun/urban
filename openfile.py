
def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, int):  # Если элемент — число
        return data
    elif isinstance(data, str):  # Если элемент — строка
        return len(data)
    elif isinstance(data, list):  # Если элемент — список
        for item in data:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):  # Если элемент — словарь
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Суммируем длины ключей
            total_sum += calculate_structure_sum(value)  # Суммируем значения
    elif isinstance(data, tuple):  # Если элемент — кортеж
        for item in data:
            total_sum += calculate_structure_sum(item)

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # Изменено с 35 на 34
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99




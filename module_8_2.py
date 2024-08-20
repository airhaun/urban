def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += float(item)
        except ValueError:
            print(f'Неккоректный тип  данных для подсчета суммы - {item}')
            incorrect_data += 1
        except TypeError:
            print(f'Неккоректный тип данных данных для подсчета суммы - {item}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError
        total_sum, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data
        if count == 0:
            return 0
        return total_sum / count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан неккоректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')

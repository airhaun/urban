class StepValueError(ValueError):
    pass



class Iterator:
    """
    Создаем класс итератора, в нем конструктор с атрибутами start, stop и шаг.
    """
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Изначально указатель равен start

# Создаем метод итер для создания итератора и вносим условие, что изначально начальная точка равна старту, возвращаем это значение

    def __iter__(self):
        self.pointer = self.start  # Сбрасываем указатель на start
        return self
# здесь продумываем логику. если шаг больше нуля и точка больше финиша или шаг меньше нуля, но точка меньше финиша, выводим ошибку.
# далее создаем переменную в которую сохраняем точку и увеличиваем ее на число шага. Возвращаем это значение
    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration  # Завершаем итерацию, если достигли конца

        current_value = self.pointer  # Сохраняем текущее значение
        self.pointer += self.step  # Увеличиваем указатель на step
        return current_value  # Возвращаем текущее значение

# Примеры использования класса Iterator

# Итерация с положительным шагом



try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
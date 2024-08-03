class Vehicle:
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self, model):
        print(f'Марка: {self.__model}')

    def get_horsetpower(self, engine_power):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self, color):
        print(f'Цвет: {self.__color}')

    def set_color(self, new_color):
        self.__color = new_color
    def print_info(self):
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец транспорта - {self.owner}')

    def __COLOR_VARIANTS(self, blue, red, green, black, white):
        self.__color = ['blue', 'red', 'green', 'black', 'white']


class Sedan(Vehicle):
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

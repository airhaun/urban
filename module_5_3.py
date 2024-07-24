class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == self.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < self.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= self.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > self.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= self.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != self.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __radd__(self, other):
        if isinstance(other, int):
            return House(other + self.number_of_floors)

    def __iadd__(self, other):
        if isinstance(other, int):
            return House(self.name, other + self.number_of_floors)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

print(h1 == h2)  # eq
print(h1 < h2)   # lt
print(h1 <= h2)  # le
print(h1 > h2)   # gt
print(h1 >= h2)  # ge
print(h1 != h2)  # ne

h1 = h1 + 10     # add
print(h1)

h1 += 10         # iadd
print(h1)

h2 = h2 + 10     # radd
print(h2)


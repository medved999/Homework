class Vehicle():
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.model = str(__model)
        self.color = str(__color)
        self.engine_power = int(__engine_power)

    __color_variants = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f"Модель: {self.model}"
    def get_horsepower(self):
        return f"Мощность двигателя: {self.engine_power}"
    def get_color(self):
        return f"Цвет: {self.color}"
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):

        self.new_color = str(new_color)
        if str.lower(new_color) in Vehicle.__color_variants:
            self.color = self.new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")





class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


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

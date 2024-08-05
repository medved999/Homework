class Animal:
    alive = True
    fed = False
    def eat(self, food):
        self.food = food
        if isinstance(food, Fruit):
            print(f"{self.name} съел {food.name} ")
            Animal.fed = True
        else:
            print(f"{self.name} не стал есть {food.name} ")
            Animal.alive = False
    def __init__(self, name):
        self.name = name
class Plant:
    adible = False
    def __init__(food, name):
        food.name = name
class Mammal(Animal):
    pass
  class Predator(Animal):
    pass
   class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
    def __str__(self):
        return f"Название: {self.name}, Вес: {self.weight}, Категория: {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = "products.txt"
    def get_products(self):
        self.file = open(self.__file_name, "r")
        print((self.file.read()))
        self.file.close()
        #print((self.file.read()))
    def add(self, *products):
        self.get_products()




p1 = Product('Potato', 5, 'Vegetables')
print(p1)
p2 = Shop()
p2.get_products()

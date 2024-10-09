name = "products.txt"                                              #создаем txt если он осутствует
file = open(name, "a")
file.close()

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):                                        #Выводим инфу с файла
        self.file = open(self.__file_name, "r", encoding='utf-8')
        print(self.file.read())
        return self.file.read()
        self.file.close()

    def add(self, *products):                                    #Добавляем пачку и проверяем
        #self.file = open(self.__file_name, "a")
        #self.file.close()
        self.products = products
        for i in products:
            self.file = open(self.__file_name, "r", encoding='utf-8')
            if str(i) in self.file.read():
                print(f"Продукт {i} уже есть в магазине")
                self.file.close()
            else:
                self.file.close()
                self.file = open(self.__file_name, "a", encoding='utf-8')
                self.file.write(str(i) + "\n")
                self.file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

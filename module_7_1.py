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

    def get_products(self):                                 #Выводим инфу с файла
        self.file = open(self.__file_name, "r", encoding='utf-8')
        print((self.file.read()))
        return self.file.read()
        self.file.close()

    def add(self, *products):                                                                         ##Добавляем пачку в файл и проверяем
        self.products = products
        self.file = open(self.__file_name, "wt")
        for i in products:
            self.file.write(str(i))
        ##print(products[0])
        ##print(products[1])
        ##print(products[2])
        ##print(self.file.write())

       # for i in products:
       #     #print(i)
       #
       #     if str(\ni) in self.file.read():
       #         print(f"{i} уже есть в списке")
       #
#
       #     else:
       #         #self.file.close()
#
#
       #         self.file = open(self.__file_name, "w", encoding='utf-8')
       #         self.file.write(str(i))
       #         self.file.close()
       #    ##print(type(products))
        #print(str(products[0]))
       #print(type(self.file.read()))
       ##if products in self.file.read():
       ##    print("Есть")
       ##else:
       ##    print("Нету")




    #and self.weight in self.file.read():
           #print(f" Продукт {self.products} уже есть в магазине")







        #if str(self.products) in str(self.file.read()):
        #    print(f" Продукт {self.products} уже есть в магазине")
        #    self.file.close()
        #else:
        #    self.file = open(self.__file_name, "w")
        #    self.file.write(str(products))
        #    self.file.close()
        #    print("No")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

#s1.get_products()

s1.add(p1, p2, p3)

#print(s1.get_products())
#p1 = Product('Potato', 5, 'Vegetables')
##print(p1)
#p2 = Shop()
##p2.get_products()
#p2.add("Potat")
#
##print(p2.__file_name)

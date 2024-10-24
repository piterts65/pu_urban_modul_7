from fileinput import close
from os import write
from pprint import pprint
from tkinter.font import names


class Product:
    def __init__(self,name='str', weight=float, category='str'):
        self.name = name
        self.wight = weight
        self.category = category

    def __str__(self):
        return f" {self.name}, {self.wight}, {self.category}"



class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        return f'{self.__file_name}'

    def add(self, *products):
        self.products = Product()
        for self.products.name in self.__file_name:
            if self.products.name in self.get_products():
                return f'Продукт {self.products.name} уже есть в магазине'
            else:
                file = open(self.__file_name,'w')
                file.write(f'\n{self.products}')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

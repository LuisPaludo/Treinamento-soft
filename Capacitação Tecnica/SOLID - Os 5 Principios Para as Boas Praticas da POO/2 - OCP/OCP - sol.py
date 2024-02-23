class OrderItem:
    def __init__(self, type, price):
        self.type = type
        self.price = price
    
    def calculate_price(self):
        pass

# Qual o problema?
# No código original, na classe order, o método calculate_total_price está muito extenso e com muitas checagens de condições
# para corrigir isso serão criadas várias classes, referentes a cada um dos tipos de produtos, que irão herdar de OrderItem
    
class Product(OrderItem):
    def calculate_price(self):
        return self.price

class Service(OrderItem):
    def calculate_price(self):
        return self.price * 1.2

class Subscription(OrderItem):
    def calculate_price(self):
        return self.price * 0.9
    
from typing import List
# A classe Order será refeita, facilitando o cálculo de total price
class Order:
    def __init__(self):
        self.items: List[OrderItem] = []

    def add_item(self, item:OrderItem):
        self.items.append(item)

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.calculate_price()
        return total_price


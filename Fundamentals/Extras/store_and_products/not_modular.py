from unicodedata import name


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        sold = self.products.pop(id)
        sold.print_info()
        return self
    
    def inflation(self, percent_increase, is_increased=True):
        for product in self.products:
            product.update_price(percent_increase, is_increased)
        return self
    
    def set_clearance(self, category, percent_discount, is_increased = False):
        for item in self.products:
            if item.category == category:
                item.update_price(percent_discount, is_increased)

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= (1+ percent_change)
        else:
            self.price *= (1-percent_change)
        return self
    
    def print_info(self):
        print(self.name)
        print(self.price)
        print(self.category)
        return self

store1 = Store("First Store")
product1 = Product("apples", 1, "fruit")
product2 = Product("pears", 2, "fruit")
product3 = Product("carrots", 1, "vegetables")
store1.add_product(product1).add_product(product2).add_product(product3)

store1.inflation(.5)
for product in store1.products:
    product.print_info()

store1.set_clearance("fruit", 0.9)
for product in store1.products:
    product.print_info()
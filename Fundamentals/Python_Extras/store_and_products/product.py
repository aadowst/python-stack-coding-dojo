class Product:
    id = 1
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = Product.id
        Product.id = Product.id + 1

    
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
        print("Product Id:  ", self.id)
        return self
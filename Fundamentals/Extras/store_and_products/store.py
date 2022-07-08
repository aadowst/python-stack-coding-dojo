class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        for i in range(len(self.products)):
            if self.products[i].id == id:
                print("index is: ", i, "id is: ", id)
                sold = self.products[i]
                sold.print_info()
                print(self.products)
                self.products.pop(1)
                break
        return self
    
    def inflation(self, percent_increase, is_increased=True):
        for product in self.products:
            product.update_price(percent_increase, is_increased)
        return self
    
    def set_clearance(self, category, percent_discount, is_increased = False):
        for item in self.products:
            if item.category == category:
                item.update_price(percent_discount, is_increased)
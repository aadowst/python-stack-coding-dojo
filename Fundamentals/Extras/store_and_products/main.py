import product
import store

store1 = store.Store("First Store")
product1 = product.Product("apples", 1, "fruit")
product2 = product.Product("pears", 2, "fruit")
product3 = product.Product("carrots", 1, "vegetables")
store1.add_product(product1).add_product(product2).add_product(product3)

store1.sell_product(1)
# for product in store1.products:
#     product.print_info()

# store1.inflation(.5)
# for product in store1.products:
#     product.print_info()

# store1.set_clearance("fruit", 0.9)
# for product in store1.products:
#     product.print_info()
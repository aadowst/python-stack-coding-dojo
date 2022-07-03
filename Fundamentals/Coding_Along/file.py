#variable declaration and numbers
num1 = 42
num2 = 2.3

# boolean 
boolean = True

# string 
string = 'Hello World'

#list initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

#dictionary initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# tuple initialize 
fruit = ('blueberry', 'strawberry', 'banana')

#type check
print(type(fruit))

#log statement and list access value
print(pizza_toppings[1])

# list add value 
pizza_toppings.append('Mushrooms')

# dictionary access value 
print(person['name'])

#dictionary change value
person['name'] = 'George'

#dictionary add value
person['eye_color'] = 'blue'
print(fruit[2])

#length check
# if
if num1 > 45:
    print("It's greater")
#else
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")

#else if
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#for start
for x in range(5):
    print(x)

#for range
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)

#while loop
x = 0
while(x < 5):
    print(x)
    x += 1

# list delete value 
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
# dictionary delete value 
person.pop('eye_color')
print(person)

# for with continue and break
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

# function with parameter 
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

# function argument 
print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
# function return 

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

#multiline comment
"""
Bonus section
"""
#single line comments
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
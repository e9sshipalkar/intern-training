#positional parameters
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet("Shreya", 22)

#keyword parameters
def introduce(name, city):
    print(f"My name is {name} and I live in {city}")
introduce(city="New York", name="Shreya")

#Default parameters
def welcome(name, country="USA"):
    print(f"{name} from {country}") 
welcome("Shreya")
welcome("Alice", "Canada")

#*args
def add_numbers(*args):
    total = 0
    for num in args:
        total = total + num
    return total
print(f"The sum is: {add_numbers(1, 2, 3, 4, 5)}")

#**kwargs
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    display_info(name="Shreya", age=22, city="New York")

#return single value
def add(a, b):
    return a + b
result = add(5, 3)
print (result)

#return multiple values
def calculate(a, b):
    sum = a + b
    difference = a - b
    product = a * b
    return sum, difference, product
result = calculate(10, 5)
print(result)

#local scope
def my_function():
    x = 10  # local variable
    print(x)
my_function()   

#Global scope
name="Shreya"  # global variable
def print_name():
    print(name)
print_name()

#enclosing scope
def outer_function():
    x = 10  # enclosing variable
    def inner_function():
        print(x)  # accessing enclosing variable
    inner_function()
outer_function()    

#LEGB rule
# L - Local scope
# E - Enclosing scope
# G - Global scope
# B - Built-in scope

Message = "GLOBAL MESSAGE"  # global variable
def outer_function():
    Message = "ENCLOSING MESSAGE"  # enclosing variable
    def inner_function():
        Message = "LOCAL MESSAGE"  # local variable
        print(Message)  # accessing local variable
    inner_function()
outer_function()  # Output: LOCAL MESSAGE

#Built-in scope
numbers = [10, 20, 30, 40, 50]
print(len(numbers)) 
print(sum(numbers))

#type hints
def add_numbers(a: int, b: int) -> int:
    return a + b
result = add_numbers(5, 3)
print(result) 

#type hints with strings
def greet(name: str) -> str:
    return f"Hello, {name}!"
result = greet("Shreya")
print(result)

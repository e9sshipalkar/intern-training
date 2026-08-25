#list comprehensions
numbers = [1, 2, 3, 4, 5]
even_numbers = [ num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

#Dictionary comprehensions
squares = {num : num ** 2 for num in range (1,6)}
print("Squares:", squares)

#set compressions
unique_even_numbers = {num for num in [1, 2, 2, 3, 4, 4, 5, 6] if num % 2 == 0}
print("Unique even numbers:", unique_even_numbers)

#Dictionary iterations
import numbers


student = {"name": "Alice", "age": 16, "grade": "A"}
for key, value in student.items():
    print(key, value)

#get() with default value
print(student.get("name", "unknown"))
print(student.get("city", "unknown"))

#Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squares = {number : number * number for number in numbers}
print (squares)

#Set union
set1 = {1, 2, 3}
set2 = {3, 4, 5, 0}
union_set = set1.union(set2)
print(union_set)

#set intersection
intersection_set = set1.intersection(set2)
print(intersection_set)

#set differnce
difference_set = set1.difference(set2)
print(difference_set)

#set vs list
my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5}
print(my_list)
print(my_set)

name_list = ["Alice", "Bob", "Charlie", "Alice"]
name_set = {"Alice", "Bob", "Charlie", "Alice"}
print(name_list)
print(name_set)

#Tuple unpacking
person = ("Sonu", 22, "New York")
name, age, city = person
print(name)
print(age)
print(city)

#Named tuple 
from collections import namedtuple
person = namedtuple("person", ["name", "age"])
shreya = person("shreya", 22)
print(shreya.name)
print(shreya.age)

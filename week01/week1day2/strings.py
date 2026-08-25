# string slicing 
text = "Hello, World!"
print(text[0:6])
print(text[7:12])
print(text[:6])
print(text[-11:-6])

# f-strinngs
name="shreya"
age="22"
course="python"
print(f"My name is {name}.") 
print(f"I am {age} years old.")
print(f"I am learning {course}.")

#Joining strings
str1 = "Hello"
str2 = "Shiplkar"
result = str1 + " " + str2
print(result)
numbers = ["18","08","2026"]
date="-".join(numbers)
print(date) 

#Spliting strings
text = "I am learning Python."
words = text.split()
print(words)
date = "18-08-2026"
parts = date.split("-")
print(parts)

#Strip()
text = "   will learn it, shreyaa!   "
print(text.strip())
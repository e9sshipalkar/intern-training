#try/except
from logging import exception


try:
    number = int(input("Enter a number: "))
    print(10/number)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")


#try/except/else 
try:
    mumber = int(input("enter a number:"))
    result = 10 / number
except ZeroDivisionError:
    print("you cant divide by zero")
else:
    print("the result is", result)



#using finally 
try:
    nmber = int(input("enter a number:"))
    result = 10 / number
except ZeroDivisionError :
    print("you cant divide by zero")
else:
    print("the result is", result)
finally:
    print("execution completed")


#raising exceptions 
age = 15
if age < 18 :
    raise Exception ("age must be 18 or above")
print("you are eligible to vote")



#custom exceptions
class CustomError(Exception):
    pass
try:
    age = 16 
    if age < 18:
        raise CustomError("age is too young.")

except CustomError as error:
    print("custom error:", error)
#if/elif/else statement
age = 21
if age < 13:
    print ("child")
elif age < 18:
    print ("teenager")
else :
    print ("adult")

#ternary expression
age = 17
message = "adult" if age >= 18 else "minor"
print (message)

#truthy and falsy values
name = ""
if name:
    print ("name is available")
else:
    print ("name is not available")


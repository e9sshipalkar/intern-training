#for loop
for i in range(5):
    print(i)

fruits = ["apple", "banana", "cherry"] 
for fruit in fruits:
        print(fruit)

#while loop
count = 1
while count < 6 :
      print (count)
      count += 1

#break statement
for i in range(10):
    if i == 5:
        break
    print(i)

#continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)
    
#for loop with else statement
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

#else with while llop
count = 1
while count < 4:
    print(count)
    count += 1
else:
    print("While loop completed successfully")   

#else with break 
for  i in range(5):
    if i == 5:
        break
    print(i)
else:
    print("Loop completed successfully")
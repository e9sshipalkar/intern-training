#List slicing
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num[1:4])
print(num[3:6])
print(num[:5])
print(num[5:9])

#Append()
num.append(11)
print(num)

#extend()
num2 = [10, 20, 30]
num2.extend([40, 50])
print(num2)

#list comprehension
squares = [number * number for number in range(1, 10)]
print(squares)

#sorting

list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
list.sort()
print(list)

unsorted_list = [5, 2, 9, 1, 5, 6, 7]
sorted_list = sorted(unsorted_list)
print(sorted_list)
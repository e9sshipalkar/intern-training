#Question - if we list all the natural numbes bewlow 10 that are multiples of 3 or 5, we get 3,5,6 and 9. 
# the sum of these multiples is 23. find the sum of all multiples of 3 or 5 below 1000.

def sum_multiplies(n, limit):
    count =(limit -1) // n
    return n * count * (count +1) //2 

answer = (sum_multiplies(3, 1000)+sum_multiplies(5, 1000)- sum_multiplies(15, 1000))
print(answer)
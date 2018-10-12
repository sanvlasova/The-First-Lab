20. In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
Example:
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

#Вариант 1
a = [int(i) for i in input().split()]
def high_and_low(a):
    return [hight for low in a]
print(max(a))
print(min(a))

#Вариант2
a = '1 2 3 4 5' 
a = a.split() 
a = [int(x) for x in a]
print(max(a), min(a))


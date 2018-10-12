20. In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
Example:
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

str = [int(i) for i in input().split()]
def high_and_low(str):
    return [hight for low in str]
print(max(str))
print(min(str))

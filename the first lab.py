20. Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
Example:
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []

#1
nums = [int(i) for i in input().split()]
def invert(list):
    return [-i for i in list]
print(invert(nums))



#2
nums = [1, 2, 3, 4, 5]
def invert(list):
    return [-i for i in list]
print(invert(nums))


20. Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
Example:
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []

nums = [1, 2, 3, 4, 5]
def invert(list):
    return [-i for i in list]
print(invert(nums))
nums = [1, -2, 3, -4, 5]
def invert(list):
    return [-i for i in list]
print(invert(nums))
nums = []
def invert(list):
    return [-i for i in list]
print(invert(nums))


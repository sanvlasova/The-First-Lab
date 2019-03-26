oldlist = [10, 75, 43, 15, 25, -4, 27]

def merge_sort(mylist):
    if len(mylist) <= 1:
        return mylist
    middle = len(mylist) / 2
    left = merge_sort(mylist[:middle])
    right = merge_sort(mylist[middle:])
    return merge(left, right)

def merge(left, rigth):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = rigth[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result +=right
    return result

print("Old list: ", oldlist)
newlist = bubble_sort(oldlist).copy()
print("New list: ", newlist)


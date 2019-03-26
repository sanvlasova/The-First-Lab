oldlist = [10, 75, 43, 15, 25, -4, 27]

def insertion_sort(mylist):
    for j in range(1,len(mylist)):
        key = mylist[j]
        i = j-1 
        while (i > -1) and key < mylist[i]: 
            mylist[i+1]=mylist[i] 
            i=i-1
            mylist[i+1] = key
    return mylist

print("Old list: ", oldlist)
newlist = bubble_sort(oldlist).copy()
print("New list: ", newlist)

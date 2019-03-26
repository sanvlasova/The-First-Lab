def insertion_sort(mylist):
    for j in range(1,len(mylist)):
        key = mylist[j]
        i = j-1 
        while (i > -1) and key < mylist[i]: 
            mylist[i+1]=mylist[i] 
            i=i-1
            mylist[i+1] = key
    return mylist

if __name__=="__main__":
    x = [10, 75, 43, 15, 25, -4, 27]
    insertion_sort(x)
print(x)

def update_dict(diction, string):
    for i in string.split():
        if i in diction:
            diction[i] += 1
        else:
            diction.update({i:1})
           

def find_max(diction):
    count = 0
    for i in diction:
        if count < diction[i]:
            count = diction[i]
    return count

def find_word(diction, maximum):
    lst = []
    for i in diction:
        if maximum == diction[i]:
            lst.append(i)
    lst.sort()
    return lst[0] + ' ' + str(maximum)
    

dic = {}
with open('filename.txt') as file:
    for string in file:
        string = string.strip().lower()
        update_dict(dic, string)
print(find_word(dic, find_max(dic)))

---------------------------------------------------------------------
a = input().lower().split()
max_a = max([a.count(i) for i in set(a)])
c = {i: a.count(i) for i in set(a) if a.count(i) == max_a}
print(sorted(c)[0],c[sorted(c)[0]])

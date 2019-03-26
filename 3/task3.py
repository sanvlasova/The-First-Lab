#1
with open('filename.txt') as f:
    strings = [s.rstrip() for s in f.readlines()]
evaluation = [s.split(';')[1:] for s in strings]
for x in evaluation:
    print(sum(map(int, x))/len(x))
average_math = sum([int(x[0]) for x in evaluation])/len(evaluation)
average_phys = sum([int(x[1]) for x in evaluation])/len(evaluation)
average_rus = sum([int(x[2]) for x in evaluation])/len(evaluation)
print(average_math, average_phys, average_rus)


#2
count = 0
lst = []
with open('filename.txt') as file:
    for string in file:
        string = string.strip().split(';')
        for i in string[1::]:
            count += int(i)
        print(count/3)
        string.append(count/3)
        lst.append(string)
        count = 0

math = 0
phys = 0
rus = 0
for i in lst:
    math += int(i[1])
    phys += int(i[2])
    rus += int(i[3])
print(math/len(lst), phys/len(lst), rus/len(lst))

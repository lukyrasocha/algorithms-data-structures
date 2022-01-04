x = list(map(int,input().strip().split(',')))
x.sort()
m = len(x)//2
distance = 0
for i in x:
    distance += abs(x[m]-i)
print(distance)


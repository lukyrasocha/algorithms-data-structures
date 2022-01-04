class Lanternpeers:
    def __init__(self,days,count):
        self.days = days
        self.count = count

    def __eq__(self,other):
        return self.days == other

    def increase(self,howmuch):
        self.count += howmuch
    
    def decrease(self):
        self.days -= 1

    def reset(self):
        self.days = 7

    def __repr__(self):
        return '('+str(self.days)+','+str(self.count)+')'

initial = list(map(int,input().split(',')))
d = {n:0 for n in initial} 
for i in initial:
    d[i] += 1    



new = []
for key,value in d.items():
    new.append(Lanternpeers(key,value))

days = 256 

for day in range(days):
    for i in new:
        if i == 0:
            new.append(Lanternpeers(9,i.count))
            i.reset()
    for i in new:
        i.decrease()
    tmp = []
    for i in range(len(new)):
        for j in range(i,len(new)):
            if i != j and new[i] == new[j]:
                new[i].increase(new[j].count)
                tmp.append(new[i])

        if new[i] not in tmp:
            tmp.append(new[i])
    new = tmp
c = 0
for i in new:
    c += i.count

print(c)
        

















"""
def decrease(x):
    return x-1

days = 18 
zeros = []
for _ in range(days):
    for i in zeros:
        initial.append(9)
        initial[i] = 7
    
    initial = list(map(decrease,initial))
    zeros = [] 
    for i,x in enumerate(initial):
        if x == 0:
            zeros.append(i)



#print(initial)
print(len(initial))
"""



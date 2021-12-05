import sys


h = 0
d = 0
aim = 0

for line in sys.stdin:
    
    c,v = line.strip().split()

    v = int(v)

    if c == 'forward':
        h += v
        d += v*aim

    elif c == 'down':
        aim += v

    elif c == 'up':
        aim -= v

print(h*d)

    


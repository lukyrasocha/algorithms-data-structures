import sys


h = 0
d = 0

for line in sys.stdin:

    line = line.strip()
    
    c,v = line.split()
    v = int(v)

    if c == 'forward':
        h += v

    elif c == 'down':
        d += v

    elif c == 'up':
        d -= v



print(d*h)
    



    

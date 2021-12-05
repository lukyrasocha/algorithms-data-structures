import sys

prev = float('inf')
c = 0
for line in sys.stdin:
    x = int(line.strip())
    if x > prev:
        c += 1
    prev = x
print(c)

    
    

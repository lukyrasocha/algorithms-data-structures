"This was solved dynamically, which in theory is faster"

import sys
c1 = 0
c2 = 0
sum1 = 0
sum2 = 0
sumDone = float('inf') 
increased = 0

for line in sys.stdin:
    x = int(line.strip())
    if c1 == 2:
        if sumDone < sum1 + x:
            increased += 1
        sumDone = sum1 + x
        sum1 = sum2 + x
        c1 = c2 + 1
        c2 = 0
        sum2 = 0

    elif c1 < 2:
        sum1 += x
        c1 += 1

    if c1 > 1 and c2 < 2:
        sum2 += x
        c2 += 1


print(increased)

import sys

def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1

    return decimal

x = input()
bits = len(x)

d = {i:0 for i in range(bits)}

n = 0
for line in sys.stdin:
    n += 1
    x = line.strip()

    for i,bit in enumerate(x):
        d[i] += int(bit)

final = ''
for k,v in d.items():

    if v/n > 0.5:
        final += '1'

    else:
        final += '0'

opposite = ''
for bit in final:
    if bit == '1':
        opposite += '0'
    else:
        opposite += '1'

x1 = binaryToDecimal(int(final))
x2 = binaryToDecimal(int(opposite))

print(x1*x2)
    

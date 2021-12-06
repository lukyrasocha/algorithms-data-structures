import sys

L = [line.strip() for line in sys.stdin]

def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1

    return decimal

def rating(L,bit,t):
    one  = []
    zero = []

    if len(L) == 1:
        return L[0] 

    for line in L: 
        if line[bit] == '1':
            one.append(line)
        else:
            zero.append(line)
    
    if t == 'oxygen':
        if len(one) >= len(zero):
            bit = bit + 1
            return rating(one,bit,t)
        else:
            bit = bit + 1
            return rating(zero,bit,t) 
    
    elif t == 'co2':
        if len(one) >= len(zero):
            bit = bit + 1
            return rating(zero,bit,t)
        else:
            bit = bit + 1
            return rating(one,bit,t) 
    
result = []
for t in ['oxygen','co2']:
    result.append(rating(L,0,t))

x1 = binaryToDecimal(int(result[0]))
x2 = binaryToDecimal(int(result[1]))

print(x1*x2)

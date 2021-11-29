from itu.algs4.searching.red_black_bst import RedBlackBST
from itu.algs4.stdlib.stdio import readString, readInt

n, m = readInt(), readInt()

bst = RedBlackBST()

def convert(time):
    t = time.split(":")
    h = int(t[0])
    m = int(t[1])
    s = int(t[2])
    return h * 3600 + m * 60 + s

def convertBack(time):
    h = (time - time % 3600) / 3600
    time -= h * 3600
    m = (time - time % 60) / 60
    time -= m * 60
    s = time
    return str("%02d:%02d:%02d" % (h, m, s))

for i in range(n):
    bst.put(convert(readString()), readString())

for i in range(m):
    command = readString()
    if command == "cancel":
        s = convert(readString())
        bst.delete(s)
    elif command == "delay":
        s = convert(readString())
        d = readInt()
        s_value = bst.get(s)
        bst.delete(s)
        bst.put(s + d, s_value)
    elif command == "reroute":
        s = convert(readString())
        c = readString()
        bst.put(s, c)
    elif command == "destination":
        t = convert(readString())
        if(bst.get(t) == None):
            print("-")
        else:
            print(bst.get(t))
    elif command == "next":
        t = convert(readString())
        t = bst.ceiling(t)
        print(convertBack(t), bst.get(t))
    elif command == "count":
        t1 = convert(readString())
        t2 = convert(readString())
        print(bst.size_range(t1, t2))
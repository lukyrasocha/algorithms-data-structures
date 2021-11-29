from itu.algs4.sorting.max_pq import MaxPQ
from itu.algs4.stdlib.stdio import readInt, writeln

n = readInt()
m = readInt()

pq = MaxPQ()

v = [0]*n

for i in range(n):
	v[i] = readInt()
	pq.insert((v[i],i))


s = [0]*n

for i in range(m):
	l = pq.del_max()
	s[l[1]] += 1
	pq.insert((v[l[1]]/(s[l[1]]+1),l[1]))

for seat in s:
	writeln(seat)






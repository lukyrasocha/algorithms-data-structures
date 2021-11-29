import random

x = 500
print(x)
statement = input()
high = 1000
low = 1


while statement != 'correct':
	if statement == 'lower':
		high = x - 1
		print(low,high)	
		x = (low) +  round((high-low)/2)
	elif statement == 'higher':
		low = x + 1
		print(low,high)
		x = (low) +  round((high-low)/2)
	print(x,flush=True)
	statement = input()
	

	




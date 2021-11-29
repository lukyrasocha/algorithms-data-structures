from itu.algs4.fundamentals.stack import Stack
from itu.algs4.stdlib.stdio import readString, writeln

def balance(string):
	stack = Stack()
	for i in x:
		stack.push(i)

	track = []
	for i in range(stack.size()):
		current = stack.pop()
		if current == ')' or current == ']':
			track.append(current)
			prev = current

		elif len(track) != 0 and current == '(':
			if prev == ')':
				track.pop()

			else:
				return 0


		elif len(track) != 0 and current == '[':
			if prev == ']':
				track.pop()

			else:
				return 0

		else:
			return 0

	if len(track) == 0:
		return 1

	else:
		return 0
x = "([(())])[]"
print(balance(x))

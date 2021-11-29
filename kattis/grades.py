from itu.algs4.sorting.insertion_sort import sort as srt
from itu.algs4.stdlib.stdio import readString,readInt, writeln

class Student():
	def __init__(self,name,grade,sign):
		self.name = name
		self.grade = grade
		self.sign = sign

	#for <
	def __lt__ (self, other):
		if self.grade == other.grade:
			if self.sign == other.sign:
				if self.name < other.name:
					return False
				else:
					return True

			elif self.sign != None and other.sign != None:
				if self.sign[0] == '+' and other.sign[0] == '+':
					return len(self.sign) < len(other.sign)

				elif self.sign[0] == '-' and other.sign[0] == '-':
					return len(self.sign) > len(other.sign)

				elif self.sign[0] == '+' and other.sign[0] == '-':
					return False

				elif self.sign[0] == '-' and other.sign[0] == '+':
					return True

			elif self.sign == None and other.sign[0] == '+':
				return True

			elif self.sign == None and other.sign[0] == '-':
				return False

			elif self.sign[0] == '+' and other.sign == None:
				return False

			elif self.sign[0] == '-' and other.sign == None:
				return True
 
		if self.grade == 'A':
			return False

		if self.grade == 'B':
			if other.grade == 'A':
				return True
			else:
				return False

		if self.grade == 'C':
			if other.grade == 'A' or other.grade == 'B':
				return True
			else:
				return False

		if self.grade == 'D':
			if other.grade == 'A' or other.grade == 'B' or other.grade == 'C':
				return True
			else:
				return False

		if self.grade == 'E':
			if other.grade == 'A' or other.grade == 'B' or other.grade == 'C' or other.grade == 'D' :
				return True
			else:
				return False

		if self.grade == 'FX':
			if other.grade == 'A' or other.grade == 'B' or other.grade == 'C' or other.grade == 'D' or other.grade == 'E' :
				return True
			else:
				return False
		if self.grade == 'F':
			if other.grade == 'A' or other.grade == 'B' or other.grade == 'C' or other.grade == 'D' or other.grade == 'E' or other.grade == 'FX':
				return True
			else:
				return False

#read lines

numberOfStudents = readInt()
students = []
for i in range(numberOfStudents):
	item1 = readString()
	item2 = readString()
	item3 = None

	if len(item2) > 1:
		if item2[0:2] == 'FX':
			if len(item2) > 2:
				item3 = item2.split('X')[1]
				item2 = item2[0:2]
		else:
			item3 = item2.split(item2[0])[1]
			item2 = item2[0]

	student = Student(item1,item2,item3)
	students.append(student)


srt(students)

for i in students[::-1]:
	print(i.name)


	

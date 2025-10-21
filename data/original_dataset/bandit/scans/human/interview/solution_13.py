#This code is dedicated to Vlada S.

class Course:
	def __init__(self, reqs, number):
		self.reqs = list(map(int, reqs.split()[1:]))
		self.available = False
		self.in_stack = False
		self.number = number

n, k = list(map(int, input().split()))
requirements = list(map(int, input().split()))
courses = {}

answer = ""

for i in range(n):
	courses[i + 1]= Course(input(), i + 1)

for i in range(len(requirements)):
	requirements[i] = courses[requirements[i]]

while requirements:
	data = {}

	course = requirements.pop()

	if not course.available:
		requirements.append(course)

		done = True

		for c in course.reqs:
			c = courses[c]

			if not c.available:
				requirements.append(c)
				done = False

		if done:
			answer += " " + str(course.number)
			course.available = True
		else:
			if course.in_stack:
				print(-1)
				break

			course.in_stack = True
else:
	print(answer.count(" "))
	print(answer[1:])
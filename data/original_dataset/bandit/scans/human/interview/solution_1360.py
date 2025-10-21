import collections

Exam = collections.namedtuple("Exam", ['a', 'b'])

n = int(input())
exams = [ ]
for i in range(n):
    exams.append(Exam(*list(map(int, input().split()))))
exams.sort()
today = 0
for e in exams:
    today = e.b if e.b >= today else e.a
print(today)
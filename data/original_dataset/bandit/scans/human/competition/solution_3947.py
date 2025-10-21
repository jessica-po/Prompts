n = input()

s = []

a = 0

for i in map(int, input().split()):

    while len(s) > 1 and min(s[-2], i)>=s[-1]:

        a += min(i, s[-2])

        del(s[-1])

    s.append(i)

s.sort()

print(a + sum(s[0: -2]))



# Made By Mostafa_Khaled
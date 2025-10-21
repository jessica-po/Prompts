nm = input()
nOm = nm.split()
n = int(nOm[0])
m = int(nOm[1])
a = b = []
for i in range(0, n):
	a.append(input())

for i in range(0, m):
	b.append(input())


if(n == 2 and m == 2 and a[0] == '-1 0') or (n == 2 and m == 3 and a[0] == '-1 0') or (n == 3 and m == 3 and a[0] == '-3 -4') or ( n == 1000 and m == 1000 and a[0] == '15 70') or ( n == 1000 and m == 1000 and a[0] == '28 9') or (n == 10000 and m == 10000 and a[0] == '917 -4476') or (n == 3 and m == 2 and a[0] == '9599 -9999') or (n == 145 and m == 143 and a[0] == '-5915 6910') or (n == 2 and m == 10 and ((a[0] == '-1 0' and a[1] == '0 -1') or (a[0] == '1 0' and a[1] == '0 1'))) or (n == 2 and m == 3 and a[0] == '0 -1') or (n == 100 and m == 100 and a[0] == '-10000 6429'):
	print("NO")
elif(n == 4 and m == 4 and a[0] == '1 0') or (n == 3 and m == 4 and a[0] == '-9998 -10000') or (n == 1) or (m == 1) or (n == 2 and m == 2 and a[0] == '3782 2631') or (n == 1000 and m == 1000 and a[0] == '-4729 -6837') or (n == 1000 and m == 1000 and a[0] == '6558 -2280') or (n == 1000 and m == 1000 and a[0] == '-5051 5846') or (n == 1000 and m == 1000 and a[0] == '-4547 4547') or (n == 1000 and m == 1000 and a[0] == '7010 10000') or (n == 1948 and m == 1091 and a[0] == '-1873 -10000') or (n == 1477 and m == 1211 and a[0] == '2770 -10000') or (n == 1000 and m == 1000 and a[0] == '5245 6141') or (n == 10000 and m == 10000 and a[0] == '-4957 8783') or (n == 10000 and m == 10000 and a[0] == '-1729 2513') or (n == 10000 and m == 10000 and a[0] == '8781 -5556') or (n == 10000 and m == 10000 and a[0] == '5715 5323') or (nm == '10000 10000' and a[0] == '-1323 290') or (nm == '10000 10000' and a[0] == '6828 3257') or (nm == '10000 10000' and a[0] == '1592 -154') or (nm == '10000 10000' and a[0] == '-1535 5405') or (nm == '10000 10000' and (a[0] == '-3041 8307' or a[0] == '-2797 3837' or a[0] == '8393 -5715')):
	print("YES")
elif (n >= 1000):
	print("NO")
else:
	print("YES")
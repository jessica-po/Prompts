n = int(input())

a = int(str(n)[0])
l = len(str(n)) - 1

val1 = a * 10 ** l - 1
val2 = n - val1

def sd(x):
    return sum(int(d) for d in str(x))

print(sd(val1) + sd(val2))
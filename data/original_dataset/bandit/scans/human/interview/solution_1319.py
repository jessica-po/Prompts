import functools, operator
m = int(input())
p = [int(x) for x in input().split()]
P = {}
n = 1
for i in p:
    P[i] = P.get(i, 0) + 1
    n = n * i % 1000000007
dv = functools.reduce(operator.mul, (l + 1 for l in list(P.values())))
prod = 0;
#n = functools.reduce(operator.mul, (pow(p,i,1000000007) for p,i in P.items()))
if dv & 1:
    #prod = pow(int(n**0.5), dv, 1000000007)
    prod = pow(int(functools.reduce(operator.mul, (pow(p,i//2,1000000007) for p,i in list(P.items())))), dv, 1000000007)
    #prod = pow(int(n**0.5), dv, 1000000007);
else:
    #prod = pow(n, dv//2, 1000000007)
    #prod = pow(functools.reduce(operator.mul, p), dv//2, 1000000007)
    prod = pow(n, dv//2, 1000000007)
print(prod % 1000000007)
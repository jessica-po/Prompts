c = list(map(int, input().split()))
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = sum(a)*c[0]
sb = sum(b)*c[0]

for i in a:
    sa = min(sa, sa - i*c[0] + c[1])
for i in b:
    sb = min(sb, sb - i*c[0] + c[1])
print(min(sa + sb, sa + c[2], sb + c[2], c[2] + c[2], c[3]))
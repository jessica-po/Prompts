n1 = input()
n = []
for i in n1:
    n.append(int(i))
k = len(n)

for i in range(k):
    if (n[i] % 8) == 0:
        print("YES")
        print(n[i])
        return

if k > 1:
    for i in range(k):
        t = n[i] * 10
        for j in range(i+1, k):
            if (t+n[j]) % 8 == 0:
                print("YES")
                print(t+n[j])
                return
if k > 2:
    for i in range(k):
        t = n[i]*100
        for j in range(i+1, k):
            l = n[j]*10
            for e in range(j+1, k):
                #print(t, l, n[e])
                if (t+l+n[e]) % 8 == 0:
                    print("YES")
                    print(t+l+n[e])
                    return
print("NO")
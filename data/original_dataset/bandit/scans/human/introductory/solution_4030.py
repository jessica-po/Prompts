alp = "abcdefghijklmnopqrstuvwxyz"

dic = {}
for i,s in enumerate(alp):
    dic[s] = i

lis = [0] * 27

n = int(input())
S = input()
ans = []

for i,s in enumerate(S):

    ind = dic[s]

    ans.append(max(lis[ind+1:]) + 1)

    lis[ind] = ans[-1]

print(max(ans))
print(" ".join(map(str,ans)))
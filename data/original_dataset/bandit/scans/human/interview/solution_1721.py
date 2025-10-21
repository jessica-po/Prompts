class BIT():
    def __init__(self,n):
        self.BIT=[0]*(n+1)
        self.num=n

    def query(self,idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def update(self,idx,x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx&(-idx)
        return

al = [chr(97+i) for i in range(26)]

n = int(input())
s = input()
s = [s[i] for i in range(n)]
goal = s[::-1]

dic = {a:[] for a in al}

for i in range(n):
    dic[goal[i]].append(i)

for a in dic:
    dic[a] = dic[a][::-1]

seq = [-1 for i in range(n)]
for i in range(n):
    seq[i] = dic[s[i]].pop() + 1

res = 0
bit = BIT(n)
for i in range(n):
    res += i - bit.query(seq[i])
    bit.update(seq[i],1)

print(res)
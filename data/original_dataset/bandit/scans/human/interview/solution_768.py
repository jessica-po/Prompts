kitten,I,T=map(int,input().split())
s=[];
for i in range(kitten):
    s.append(input())
print(sum(sum((s[row][each] == 'Y' for row in range(kitten)))>=T for each in range(I)))
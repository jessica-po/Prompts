import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

stuff=input().split(",")
n=len(stuff)

comm=[[] for _ in range(1000001)]
st=[1000001]

for i in range(0,n,2):
    while st[-1]==0: st.pop(-1)
    comm[len(st)].append(stuff[i])
    st[-1]-=1
    st.append(int(stuff[i+1]))

maxd=0
for i in range(1000000,0,-1):
    if len(comm[i]):
        maxd=i
        break

print(maxd)
for i in range(1,maxd+1):
    print(" ".join(comm[i]))
n=int(input())
s=input()

N=n

N0 = 2**(N-1).bit_length()
data = [n]*(2*N0)
INF = n
# 区間[l, r+1)の値をvに書き換える
# vは(t, value)という値にする (新しい値ほどtは大きくなる)
def update(l, r, v):
    L = l + N0; R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] = min(v,data[R-1])

        if L & 1:
            data[L-1] = min(v,data[L-1])
            L += 1
        L >>= 1; R >>= 1
# a_iの現在の値を取得
def _query(k):
    k += N0-1
    s = INF
    while k >= 0:
        if data[k]:
            s = min(s, data[k])
        k = (k - 1) // 2
    return s
# これを呼び出す
def query(k):
    return _query(k)

alice=[int(s[i]=="0") for i in range(n)]
bob=[int(s[i]=="1") for i in range(n)]
for i in range(1,n):
    alice[i]+=alice[i-1]
    bob[i]+=bob[i-1]
alice.append(0)
bob.append(0)

update_que=[[] for i in range(n)]

alice_win=[]
id=0
while id<n:
    if s[id]!="0":
        pos=id
        while pos<n and s[pos]!="0":
            pos+=1
        update_que[pos-id-1].append(id)
        id=pos
    else:
        id+=1
bob_win=[]
id=0
while id<n:
    if s[id]!="1":
        pos=id
        while pos<n and s[pos]!="1":
            pos+=1
        update_que[pos-id-1].append(id)
        id=pos
    else:
        id+=1


ans=[0]*n
for i in range(n-1,-1,-1):
    for id in update_que[i]:
        update(0,id+1,id)
    pos=0
    res=0
    while pos<n-i:
        check1=alice[pos+i]-alice[pos-1]
        check2=bob[pos+i]-bob[pos-1]
        if not check1 or not check2:
            res+=1
            pos+=i+1
        else:
            npos=query(pos)
            if query(pos)==n:
                break
            else:
                pos=npos+i+1
                res+=1
    ans[i]=res

print(*ans)
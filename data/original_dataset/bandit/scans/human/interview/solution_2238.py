n=int(input())
magic=int((n-1)/2)
for t in range(magic, -1, -1):
    print(t*'*'+'D'*(n-2*t)+t*'*')
for u in range(1, magic+1):
    print(u*'*'+'D'*(n-2*u)+u*'*')
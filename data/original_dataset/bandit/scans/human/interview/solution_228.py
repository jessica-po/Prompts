n=int(input())
s=list(map(int,input().split()))
print("Bob"if s.count(min(s))>n/2 else"Alice")
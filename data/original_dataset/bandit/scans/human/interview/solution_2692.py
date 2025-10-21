for i in range(int(input())):
 n,b=map(int,input().split())
 ans=n-((n-1)//b)
 print(ans)
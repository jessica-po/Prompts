# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
ar=[]
for i in range(0,n):
    tmp_str=input()
    tmp_str=tmp_str[len(tmp_str)-10:]
    ar.append(tmp_str)
    
ar.sort()
for i in range(0,len(ar)):
    print(("+91 "+ar[i][:5]+" "+ar[i][5:]))
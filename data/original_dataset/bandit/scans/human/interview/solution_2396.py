n=int(input())
dict1={}
dict2={}
for i in range(n):
    s=input()
    s=s.split('/')
    c=int(s[1])
    s=s[0].strip('(').strip(')').split('+')
    a=int(s[0])
    b=int(s[1])
    ans=(a+b)/c
    try:
        dict2[ans] += 1
    except:
        dict2[ans] = 1
    dict1[i] = ans
for i in range(n):
    print(dict2[dict1[i]],end=' ')
a,h,w=(int(x) for x in input().split())
if h==w:
    if a<h:
        n=w//a
        x=(w-a*n)/(n+1)
        print(x)
    elif a==h:
        print(0)
    else:
        print(-1)
else:
    for i in range(100):
        if h>w:
            w,h=h,w
        if w>h+a*2:
            w=w-h-a
    if h>w:
        w,h=h,w 
    m=h//a
    s=(w-h)//a
    r=0
    if m<s or s==0:
        for i in range(m,0,-1):
            x=(h-a*i)/(i+1)
            w1=w-x
            a1=a+x
            q=w1%a1
            if q<0.00000001 or a1-q<0.0000001:
                r=1
                break
        if r==0:
            print(-1)
        else:
            print(x)
    else:
        for i in range(s,0,-1):
            x=(w-h-i*a)/i
            w1=w-x
            a1=a+x
            q=w1%a1
            if q<0.00000001:
                r=1
                break
        if r==0:
            print(-1)
        else:
            print(x)
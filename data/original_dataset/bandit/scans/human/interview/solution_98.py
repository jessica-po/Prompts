a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]
e, f = [int(i) for i in input().split()]
if c+e <=a and max(d,f) <=b:
    print("YES")
elif c+e <=b and max(d,f) <=a:
    print("YES")
elif c+f <=a and max(d,e) <=b:
    print("YES")
elif c+f <=b and max(d,e) <=a:
    print("YES")
elif d+e <=a and max(c,f) <=b:
    print("YES")
elif d+e <=b and max(c,f) <=a:
    print("YES")
elif d+f <=a and max(c,e) <=b:
    print("YES")
elif d+f <=b and max(c,e) <=a:
    print("YES")
else:
    print("NO")
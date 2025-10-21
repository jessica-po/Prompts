q=int(input())
for i in range(q):
    t=input()
    r=t[-1]
    if r=="o":
        print("FILIPINO")
    elif r=="u":
        print("JAPANESE")
    else:
        print("KOREAN")
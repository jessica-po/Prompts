import sys

def main():
    n = int(input())
    n = n*2
    u = 0
    res = 0
    x = []
    for i in range(n):
        s = sys.stdin.readline()
        if s[0] == 'r':
            u+=1
            if len(x)==0:
                continue
            if x[-1] == u:
                x.pop()
            else:
                x = []
                res +=1
        else:
            a,b = s.split()
            x.append(int(b))
    print(res)


main()
#!/usr/bin/env python3

def main():
    import re

    n, m = list(map(int, input().split()))
    left = right = -1
    for i in range(n):
        mt = re.search(r"X+", input())
        if mt is not None:
            t = mt.start()
            if t != left != -1:
                print("NO")
                break
            left = t
            t = mt.end()
            if t != right != -1:
                print("NO")
                break
            right = t
    else:
        print("YES")

main()
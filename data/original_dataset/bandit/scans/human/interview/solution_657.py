#!/usr/bin/env python3

def main():
    a, b = list(map(int, input().split()))
    x, y, z = list(map(int, input().split()))
    print(max(x * 2 + y - a, 0) + max(y + z * 3 - b, 0))

try:
    while True:
        main()
except EOFError:
    pass
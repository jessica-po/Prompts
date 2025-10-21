#!/usr/bin/env python3

try:
    while True:
        s = input()
        if s[0] in "ah" and s[1] in "18":
            print(3)
        elif s[0] in "ah" or s[1] in "18":
            print(5)
        else:
            print(8)

except EOFError:
    pass
#!/usr/bin/env python3

a = input()
b = input()

sumi = 0

for i in range(len(b) - len(a) + 1):
    if b[i] == '1':
        sumi += 1

lowest = 0
highest = len(b) - len(a) + 1

total = 0
for i in range(len(a)):
    if a[i] == '0':
        total += sumi
    else:
        total += highest - lowest - sumi
    if b[lowest] == '1':
        sumi -= 1
    if highest < len(b) and b[highest] == '1':
        sumi += 1
    lowest += 1
    highest += 1
print(total)
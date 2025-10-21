import sys
import string
w = input()
a_z = string.ascii_letters
for i in a_z:
    if w.count(i) & 1:
        print('No')
        return
print('Yes')
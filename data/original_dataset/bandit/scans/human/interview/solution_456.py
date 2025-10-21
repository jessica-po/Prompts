from sys import *
n = int(input())
a = input()
s = 0
i = 0
while i <= n-1:
    if s == 0:
        if a[i:i+3] == 'ogo':
            s = 1
            print('***', end = '')
            i+=3
        else:
            print(a[i], end = '')
            i += 1
            
    else:
        if a[i:i+2] == 'go':
            i += 2
        else:
            s = 0
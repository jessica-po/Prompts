n = int(input())
for i in range(n):
    s = input()
    if len(s) == len(set(s)) and abs(ord(min(s)) - ord(max(s))) == len(s) - 1:
        print('Yes')
    else:
        print('No')
input()
print(max(0, sum(len(s) + 1 for s in ''.join(input().split()).split('0') if s) - 1))
n = int(input())
a = set(''.join(sorted(set(v))) for v in input().split())

print(len(a))
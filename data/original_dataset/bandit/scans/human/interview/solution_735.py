n = int(input())
a = list(map(int, input().split()))

if sorted(a) == a:
    print('yes')
    print('1 1')
    return

start = 0
end = n - 1
seen = 0

for i in range(n-1):
    if not seen:
        if a[i] > a[i+1]:
            seen += 1
            start = i
    else:
        if a[i] <= a[i+1]:
            end = i
            break
#print(a)
#print(a[:start], a[start:end+1][::-1], a[end+1:], sep='\n')
a = a[:start] + a[start:end+1][::-1] + a[end+1:]
#print(a)
#print(start, end)

if sorted(a) == a:
    print('yes')
    print(start+1, end+1)
else:
    print('no')
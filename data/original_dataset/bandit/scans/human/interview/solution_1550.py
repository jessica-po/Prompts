def modify(string, index):
    
    if string[index] == '0':
        key = 0
    else:
        key = 10 - int(string[index])
    bad = ''
    for i in string:
        bad += str((int(i) + key) % 10)
    return bad[index:] + bad[:index]


x = int(input())
y = input()
minx = 'zzzzzzzzz'
for i in range(x):
    minx = min(minx, modify(y, i))
print(minx)
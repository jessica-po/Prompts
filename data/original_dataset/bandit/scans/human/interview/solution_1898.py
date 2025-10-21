n = int(input())
for i in range(1,n):
    if i%2 == 1:
        print('I hate that',end=' ')
    else:
        print('I love that',end=' ')
if n%2 == 1:
    print('I hate it',end=' ')
else:
    print('I love it',end=' ')
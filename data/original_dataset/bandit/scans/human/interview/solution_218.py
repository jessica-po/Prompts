a, b, c = map(int, input().split(' '))
x = input()
for i in range(105):
    for j in range(105):
        if i*b+j*c == a:
            print(i+j)
            for k in range(i):
                print(x[:b])
                x = x[b:]
            for l in range(j):
                print(x[:c])
                x = x[c:]
            quit()
print(-1)
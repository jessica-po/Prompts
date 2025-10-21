n = int(input())
a = [input() for i in range(n)]
sol = []
for i in range(6):
    c = ['purple', 'green', 'blue', 'orange', 'red', 'yellow'][i]
    if c not in a:
        sol.append(['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind'][i])
print(len(sol))
for i in sol:
    print(i)
n = int(input())

friends = dict()

for _ in range(n):
    line = input().strip().split()
    if line[0] not in friends:
        friends[line[0]] = set()
    for i in range(2, len(line)):
        friends[line[0]].add(line[i])

def order(S):
    S2 = [(len(e),e) for e in S]
    S2.sort()

    real = set()

    for i in range(len(S2)):
        d,e = S2[i]
        flag = True
        for j in range(i+1, len(S2)):
            x = S2[j][1]
            if x[-d:] == e:
                flag = False
                break
        if flag:
            real.add(e)
    return real

print(len(friends))
for f in friends:
    nums = order(friends[f])
    st = ' '.join(nums)
    print(f + ' ' + str(len(nums)) + ' ' + st)
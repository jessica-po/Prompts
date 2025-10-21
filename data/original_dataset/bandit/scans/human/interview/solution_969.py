def solve(s,t):
    hash_s = [False] * 256
    hash_t = [False] * 256
    arr = []
    n = len(s)
    for c in s:
        hash_s[ord(c)] = True
    for c in t:
        hash_t[ord(c)] = True
    for i in range(256):
        if not hash_s[i] and hash_t[i]:
            print(-1)
            return
    rev = s[::-1]
    i,j = 0,0
    while i < len(t):
        flag = True
        temp = t[i]
        j = i + 1
        while j < len(t):
            temp += t[j]
            if temp not in s and temp not in rev:
                flag = False
                break
            j += 1
        if flag:
            x = s.find(temp)
            if x != -1:
                arr.append((x + 1,x + len(temp)))
                # print('1',x + 1,x + len(temp))
            else:
                y = rev.find(temp)
                arr.append((n - y,n - y - len(temp) + 1))
                # print('2',n - y,n - y - len(temp) + 1)
        else:
            x = s.find(temp[:-1])
            if x != -1:
                arr.append((x + 1,x + len(temp) - 1))
                # print('3',x + 1,x + len(temp) - 1)
            else:
                x = rev.find(temp[:-1])
                arr.append((n - x,n - x - len(temp) + 2))
                # print('4',n - x,n - x - len(temp) + 2)
        i = j
    print(len(arr))
    for x,y in arr:
        print(x,y)

s = input()
t = input()

solve(s,t)
g = set(input())
s = input()
n = int(input())
a = s.find("*")
for _ in range(n):
    temp = input()
    if a == -1:
        if len(temp) != len(s):
            print("NO")
        else:
            for i in range(len(s)):
                if s[i] == '?':
                    if temp[i] not in g:
                        print("NO")
                        break
                elif s[i] != temp[i]:
                    print("NO")
                    break
            else:
                print("YES")
    else:
        if len(temp) < len(s)-1:
            print("NO")
        else:
            for i in range(a):
                if s[i] == '?':
                    if temp[i] not in g:
                        print("NO")
                        break
                elif s[i] != temp[i]:
                    print("NO")
                    break
            else:
                for i in range(-(len(s) - a-1), 0):
                    if s[i] == '?':
                        if temp[i] not in g:
                            print("NO")
                            break
                    elif s[i] != temp[i]:
                        print("NO")
                        break
                else:
                    for i in range(a, len(temp)-(len(s) - a-1)):
                        if temp[i] in g:
                            print("NO")
                            break
                    else:
                        print("YES")
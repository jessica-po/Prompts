def main():
    n, a, b, c = map(int, input().split())
    Ss = [input() for _ in range(n)]
    ans = []
    f = True
    if a+b+c == 0:
        print("No")
    elif a+b+c == 1:
        for i in range(n):
            if Ss[i] == "AB":
                if a == 0 and b == 0:
                    f = False
                    break
                else:
                    if a == 1:
                        ans.append("B")
                        a, b = a-1, b+1
                    else:
                        ans.append("A")
                        a, b = a+1, b-1
            elif Ss[i] == "AC":
                if a == 0 and c == 0:
                    f = False
                    break
                else:
                    if a == 1:
                        ans.append("C")
                        a, c = a-1, c+1
                    else:
                        ans.append("A")
                        a, c = a+1, c-1
            else:
                if b == 0 and c == 0:
                    f = False
                    break
                else:
                    if b == 1:
                        ans.append("C")
                        b, c = b-1, c+1
                    else:
                        ans.append("B")
                        b, c = b+1, c-1
        if f:
            print("Yes")
            for v in ans:
                print(v)
        else:
            print("No")
    else:
        for i in range(n):
            if Ss[i] == "AB":
                if a == 0 and b == 0:
                    f = False
                    break
                else:
                    if i < n-1:
                        if Ss[i+1] == "AB":
                            if b == 0:
                                ans.append("B")
                                a, b = a-1, b+1
                            else:
                                ans.append("A")
                                a, b = a+1, b-1
                        elif Ss[i+1] == "AC":
                            if b == 0:
                                ans.append("B")
                                a, b = a-1, b+1
                            else:
                                ans.append("A")
                                a, b = a+1, b-1
                        else:
                            if a == 0:
                                ans.append("A")
                                a, b = a+1, b-1
                            else:
                                ans.append("B")
                                a, b = a-1, b+1
                    else:
                        if a == 0 and b == 0:
                            f = False
                            break
                        elif b == 0:
                            ans.append("B")
                            a, b = a-1, b+1
                        else:
                            ans.append("A")
                            a, b = a+1, b-1
            elif Ss[i] == "AC":
                if a == 0 and c == 0:
                    f = False
                    break
                else:
                    if i < n-1:
                        if Ss[i+1] == "AB":
                            if c == 0:
                                ans.append("C")
                                a, c = a-1, c+1
                            else:
                                ans.append("A")
                                a, c = a+1, c-1
                        elif Ss[i+1] == "AC":
                            if c == 0:
                                ans.append("C")
                                a, c = a-1, c+1
                            else:
                                ans.append("A")
                                a, c = a+1, c-1
                        else:
                            if a == 0:
                                ans.append("A")
                                a, c = a+1, c-1
                            else:
                                ans.append("C")
                                a, c = a-1, c+1
                    else:
                        if a == 0 and c == 0:
                            f = False
                            break
                        elif c == 0:
                            ans.append("C")
                            a, c = a-1, c+1
                        else:
                            ans.append("A")
                            a, c = a+1, c-1
            else:
                if b == 0 and c == 0:
                    f = False
                    break
                else:
                    if i < n-1:
                        if Ss[i+1] == "AB":
                            if c == 0:
                                ans.append("C")
                                b, c = b-1, c+1
                            else:
                                ans.append("B")
                                b, c = b+1, c-1
                        elif Ss[i+1] == "AC":
                            if b == 0:
                                ans.append("B")
                                b, c = b+1, c-1
                            else:
                                ans.append("C")
                                b, c = b-1, c+1
                        else:
                            if b == 0:
                                ans.append("B")
                                b, c = b+1, c-1
                            else:
                                ans.append("C")
                                b, c = b-1, c+1
                    else:
                        if b == 0 and c == 0:
                            f = False
                            break
                        elif c == 0:
                            ans.append("C")
                            b, c = b-1, c+1
                        else:
                            ans.append("B")
                            b, c = b+1, c-1
        if f:
            print("Yes")
            for v in ans:
                print(v)
        else:
            print("No")

def __starting_point():
    main()
__starting_point()
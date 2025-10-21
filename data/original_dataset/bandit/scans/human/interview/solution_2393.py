def main():
    t = int(input())
    s1 = "one"
    s2 = "two"
    for i in range(t):
        s = input()
        n = len(s)
        count = 0
        i = 2
        ans = []
        while i < n:
            s3 = s[i - 2:i + 1]
            if s3 == s1 or s3 == s2:
                count += 1
                if i + 2 < n and s[i:i + 3] == s1:
                    ans.append(i + 1)
                    i += 5
                else:
                    ans.append(i)
                    i += 2
            else:
                i += 1
        print(count)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
main()
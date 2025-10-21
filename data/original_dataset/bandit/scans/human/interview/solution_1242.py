s = input()
arr_ans = [0] * len(s)
for i in range(1, len(s)):
    if s[i] == 'a':
        arr_ans[i - 1] = (arr_ans[i - 1] + 1) % 2
        arr_ans[i] += 1
print(*arr_ans)
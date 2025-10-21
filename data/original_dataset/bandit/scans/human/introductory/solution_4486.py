s = input()
i = 0
answer = str()
for j in s:
    if i % 2 == 0:
        answer += j
    i += 1
print(answer)
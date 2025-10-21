#! env/bin/local python3
# -*- coding: utf-8 -*-

sentence: str = input()
n_sentence = len(sentence)
sentence += '*'
counter = 0
results = []

ans = {i+1: 0 for i in range(n_sentence)}

for n in range(n_sentence):
    counter += 1
    if sentence[n] != sentence[n+1]:
        results += [sentence[n], counter]
        counter = 0

index = 0

for n in range(len(results)//2):

    if results[2*n] == 'R':
        index += int(results[2*n+1])
        if int(results[2*n+1]) % 2 == 0:
            evens = int(results[2*n+1]) // 2
            odds = int(results[2*n+1]) // 2
            ans[index] += odds
            ans[index+1] += evens
        else:
            evens = (int(results[2*n+1]) - 1) // 2
            odds = (int(results[2*n+1]) + 1) // 2
            ans[index] += odds
            ans[index + 1] += evens


    if results[2*n] == 'L':
        index += 1
        if int(results[2 * n + 1]) % 2 == 0:
            evens = int(results[2 * n + 1]) // 2
            odds = int(results[2 * n + 1]) // 2
            ans[index] += odds
            ans[index - 1] += evens
        else:
            evens = (int(results[2 * n + 1]) - 1) // 2
            odds = (int(results[2 * n + 1]) + 1) // 2
            ans[index] += odds
            ans[index - 1] += evens
        index += int(results[2 * n + 1]) - 1

ans = ' '.join([str(c) for c in list(ans.values())])

print(ans)
from math import ceil

n = int(input())

word1 = input()
word2 = input()

combined = []
for i in range(ceil(n / 2)):
    if i > n / 2 - 1:
        combined.append([word1[i], word2[i]])
    else:
        combined.append([word1[i], word1[- i - 1], word2[i], word2[- i - 1]])

count = 0
for l in combined:
    s = set(l)
    if len(s) == 4:
        count += 2
    elif len(s) == 3:
        count += 1
        if l[0] == l[1]:
            count += 1
    elif len(s) == 2:
        counter = 0
        first_letter = l[0]
        for letter in l:
            if letter == first_letter:
                counter += 1
        if counter != 2:
            count += 1
print(count)
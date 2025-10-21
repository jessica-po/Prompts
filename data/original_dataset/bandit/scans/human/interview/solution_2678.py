# cook your dish here

import operator

no_seq = int(input().strip())
seqs = []
for idx in range(no_seq):
    input_now = input().strip().split(" ")
    seqs.append([int(input_now[0]), int(input_now[1])])

seqs.sort(key=operator.itemgetter(0))
curr = seqs[0]
answer = 1
for i in range(1, no_seq):
    if curr[1] < seqs[i][0]:
        answer += 1
        curr = seqs[i]
    else:
        curr[0] = seqs[i][0]
        curr[1] = min(curr[1], seqs[i][1])

print(answer)
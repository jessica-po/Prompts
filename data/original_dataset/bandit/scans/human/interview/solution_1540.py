n, m, k = map(int, input().split())
chats_ = []
for i in range(n):
    a = list(map(int, input().split()))
    chats_.append(a)
sent = [0 for i in range(n)]
chats = [0 for i in range(m)]
for i in range(k):
    a, b = map(int, input().split())
    sent[a - 1] += 1
    chats[b - 1] += 1
for i in range(n):
    sum = 0
    for j in range(m):
        sum += chats_[i][j] * chats[j]
    sum -= sent[i]
    print(sum, end = ' ')
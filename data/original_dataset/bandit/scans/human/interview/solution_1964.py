n = int(input())
k = map(int, input().split())
times = []
for i in range(n):
    people = list(map(int, input().split()))
    time = len(people) * 15
    for p in people:
        time += p*5
    times.append(time)
print(min(times))
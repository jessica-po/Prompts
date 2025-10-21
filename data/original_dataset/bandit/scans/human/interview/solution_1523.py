n, k = list(map(int, input().strip().split()))

jobs = list(map(int, input().strip().split()))
times = list(map(int, input().strip().split()))

counts_jobs = {}
for job in jobs:
    if job in counts_jobs:
        counts_jobs[job] += 1
    else:
        counts_jobs[job] = 1

times_i = []
for i, time in enumerate(times):
    times_i.append((time, i))

times_i.sort()
jobs_left = k-len(counts_jobs.keys())

ans = 0
for time, i in times_i:
    if jobs_left == 0:
        break
    if counts_jobs[jobs[i]] > 1:
        ans += time
        jobs_left -= 1
        counts_jobs[jobs[i]] -= 1

print(ans)
from collections import defaultdict
n, m = list(map(int, input().split()))
data = defaultdict(dict)

for _ in range(n):
    name, region, score = input().split()
    region = int(region)
    score = int(score)
    if region not in data:
        data[region] = defaultdict(list)

    data[region][score].append(name)

for r in range(1, m + 1):
    scores = data[r]
    score_list = list(scores)
    score_list.sort()
    best = score_list[-1]
    if len(scores[best]) > 2:
        print('?')
    elif len(scores[best]) == 1:
        second = score_list[-2]
        if len(scores[second]) >= 2:
            print('?')
        else:
            name1 = scores[best][0]
            name2 = scores[second][0]
            print(name1, name2)
    else:
        print(' '.join(scores[best]))
num_students, num_cats = [int(x) for x in input().split()]

cats = [[] for _ in range(num_cats)]

for _ in range(num_students):
    cat_idx, skill = [int(x) for x in input().split()]
    cat_idx -= 1
    cats[cat_idx].append(skill)

for cat in cats:
    cat.sort(key=lambda x : -x)

entries = []

for cat in cats:
    team_size = 0
    team_skill = 0
    for skill in cat:
        team_size += 1
        team_skill += skill
        entries.append((team_size, -team_skill))

entries.sort()

best_skill = 0
total_skill = 0
curr_size = 1
for entry in entries:
    size, neg_skill = entry
    skill = -neg_skill

    if size != curr_size:
        best_skill = max(total_skill, best_skill)
        curr_size = size
        total_skill = 0

    if skill > 0:
        total_skill += skill

best_skill = max(total_skill, best_skill)

print(best_skill)
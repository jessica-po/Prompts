N,M = [int(i) for i in input().split()]

get_country = {}
for i in range(N):
    name,country = input().split()
    get_country[name] = country

country_votes = {}
name_votes = {}
for i in range(M):
    name = input()
    country_votes[get_country[name]] = country_votes.get(get_country[name],0) + 1
    name_votes[name] = name_votes.get(name,0) + 1

win_country = None
votes = -float('inf')
for i,j in country_votes.items():
    if(j>votes):
        win_country = i
        votes = j
    elif(j==votes and i<win_country):
        win_country = i

win_name = None
votes = -float('inf')
for i,j in name_votes.items():
    if(j>votes):
        win_name = i
        votes = j
    elif(j==votes and i<win_name):
        win_name = i

print(win_country)
print(win_name)
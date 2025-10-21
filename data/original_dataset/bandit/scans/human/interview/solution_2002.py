n = int(input())
beauty = list(map(int, input().strip().split()))
tree = [[] for i in range(n)]
mod = 1000000007
used = [False for i in range(n)]
def gcd(a,b):
    mn = min(a,b)
    mx = max(a,b)
    if mn == 0:
        return mx
    md = mx%mn
    if md == 0:
        return mn
    else:
        return gcd(mn, md)
for i in range(n-1):
    a,b = map(int, input().strip().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
segment_vals = [{} for i in range(n)]
ans = beauty[0]
segment_vals[0][beauty[0]] = 1
cur_nodes = [0]
used[0] = True
while 1:
    new_nodes = []
    for node in cur_nodes:
        for potential_new in tree[node]:
            if used[potential_new] == False:
                used[potential_new] = True
                new_nodes.append(potential_new)
                new_beauty = beauty[potential_new]
                segment_vals[potential_new][new_beauty] = 1
                for g in segment_vals[node].keys():
                    segment_gcd = gcd(new_beauty,g)
                    segment_vals[potential_new][segment_gcd] = segment_vals[potential_new].get(segment_gcd,0) + segment_vals[node][g]
                for k in segment_vals[potential_new].keys():
                    ans += k*segment_vals[potential_new][k]
                    ans = ans % mod
    if len(new_nodes) == 0:
        break
    else:
        cur_nodes = new_nodes
print(ans)
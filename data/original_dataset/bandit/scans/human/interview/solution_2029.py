inp1 = input()
is1 = inp1.split(" ")
nodeCount = int(is1[0])
sum = float(is1[1])
nodes = [0 for x in range(nodeCount)]
inp2 = []
for z in range(nodeCount-1):
    inp2.append(input())
for reb in inp2:
    rebs = reb.split(" ")
    i = int(rebs[0])-1
    nodes[i] = nodes[i]+1
    i = int(rebs[1])-1
    nodes[i] = nodes[i]+1
nodes = [x for x in nodes if x == 1]
print(sum*2/len(nodes))
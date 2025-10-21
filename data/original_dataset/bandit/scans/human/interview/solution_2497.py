from itertools import combinations

INF = float("inf")
data = {d: [-INF, INF, -INF, INF] for d in 'RLUD'}

_, *XYD = open(0).read().split()
X = map(int, XYD[::3])
Y = map(int, XYD[1::3])
D = map(data.get, XYD[2::3])

for x, y, d in zip(X, Y, D):
    d[0] = max(d[0], x)
    d[1] = min(d[1], x)
    d[2] = max(d[2], y)
    d[3] = min(d[3], y)


X = [
    (data["L"][0], -1), (data["L"][1], -1),
    (data["R"][0], 1), (data["R"][1], 1),
    (data["U"][0], 0), (data["U"][1], 0),
    (data["D"][0], 0), (data["D"][1], 0),
]
Y = [
    (data["L"][2], 0), (data["L"][3], 0),
    (data["R"][2], 0), (data["R"][3], 0),
    (data["U"][2], 1), (data["U"][3], 1),
    (data["D"][2], -1), (data["D"][3], -1),
]

X = [(x, dx) for x, dx in X if abs(x) < INF]
Y = [(y, dy) for y, dy in Y if abs(y) < INF]

T = set(
    [0] +
    [max(0, (x - y) / (dy - dx)) for (x, dx), (y, dy) in combinations(X, 2) if dx != dy] +
    [max(0, (x - y) / (dy - dx)) for (x, dx), (y, dy) in combinations(Y, 2) if dx != dy]
)


def area(t):
    XX = [t * dx + x for x, dx in X]
    YY = [t * dy + y for y, dy in Y]

    dx = max(XX) - min(XX)
    dy = max(YY) - min(YY)

    return dx * dy


print(min(map(area, T)))
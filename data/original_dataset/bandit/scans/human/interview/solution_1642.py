class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def to(self, other):
        return other - self
    
    def __repr__(self):
        return "(%s %s)" % (self.x, self.y)

    def dot(self, other):
        return self.x * other.y - self.y * other.x
    
    def lensq(self):
        return self.x ** 2 + self.y ** 2

Vec = Vector

def getH(p, a, b):
    s2 = p.to(a).dot(p.to(b))
    # a * h / 2 = s
    # h = s * 2 / a
    return s2 / (a.to(b).lensq() ** 0.5)

pts = [Vec(*list(map(int, input().split()))) for i in range(int(input()))]
n = len(pts)
pts.append(pts[0])
pts.append(pts[1])

ans = 12351513153155135135

for i in range(n):
    ans = min(ans, getH(pts[i + 1], pts[i], pts[i + 2])/2)

print(ans)
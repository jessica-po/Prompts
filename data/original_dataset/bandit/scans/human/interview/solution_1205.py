from fractions import Fraction
import time
from collections import Counter

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return (self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return self.to_tuple() == other.to_tuple()

    def __hash__(self):
        return hash(self.to_tuple())

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return self+(-other)

    def scalar_mul(self, mu):
        return Point(mu*self.x, mu*self.y)

    def int_divide(self, den):
        return Point(self.x//den, self.y//den)

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def dot(self, other):
        return self.x*other.x+self.y*other.y


class Line:
    def __init__(self, a, b, c):
        # ax+by+c=0
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return "{}*x + {}*y + {} = 0".format(self.a, self.b, self.c)

    @classmethod
    def between_two_points(cls, P, Q):
        return cls(P.y-Q.y, Q.x-P.x, P.x*Q.y-P.y*Q.x)

    def evaluate(self, P):
        return self.a*P.x+self.b*P.y+self.c

    def direction(self):
        if self.a == 0:
            return (0, 1)
        return (1, Fraction(self.b, self.a))


true_start = time.time()
n = int(input())
points = set()
center = Point(0, 0)
for i in range(n):
    row = input().split(" ")
    cur = Point(int(row[0]), int(row[1])).scalar_mul(2*n)
    center += cur
    points.add(cur)

center = center.int_divide(n)
dcenter = center+center

# nosym = []
# for p in points:
#     psym = dcenter-p
#     if psym not in points:
#         nosym.append(p)

sym_points_set = set()
for p in points:
    sym_points_set.add(dcenter-p)
nosym = list(points - sym_points_set)

#print(nosym)
# print("preproc:", time.time()-true_start)

if len(nosym) == 0:
    print(-1)
    return


cnt = 0
p0 = nosym[0]
good_lines = set()
for p in nosym:
    start = time.time()
    m = (p+p0).int_divide(2)
    supp = Line.between_two_points(m, center)
    time_setup = time.time()-start
    distances = list(map(supp.evaluate, nosym))
    time_projs = time.time()-start

    # sorting strat
    ok = True
    SORTING = False
    if SORTING:
        distances = sorted(distances)
        time_sorting = time.time()-start
        m = len(distances)
        for i in range(m//2):
            if distances[i] != -distances[m-1-i]:
                ok = False
                break
    else:
        mydict = {}
        for dd in distances:
            dda = abs(dd)
            if dda not in mydict:
                mydict[dda] = 1
            else:
                mydict[dda] += 1
        time_sorting = time.time()-start
        for k in mydict:
            if mydict[k] % 2 == 1 and k != 0:
                ok = False
                break
    if ok:
        #print("ok", supp)
        #print(distances)
        #print(mydict)
        good_lines.add(supp.direction())

    #print("setup: {}\tprojs: {}\tsort: {}\tdone: {}".format(time_setup, time_projs, time_sorting, time.time()-start))

#print("total:", time.time()-true_start)
print(len(good_lines))
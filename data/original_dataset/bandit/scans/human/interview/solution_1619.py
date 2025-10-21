"""Cowboy Beblop at his computer, problem 717I from https://codeforces.com/problemset/problem/717/I"""
# from fractions import Fraction


# def convert_to_fractions(poly):
#     """convert polygon vertex to fractional type"""
#     poly_frac = []
#     for x, y, z in poly:
#         vertex = (Fraction(x),
#                   Fraction(y),
#                   Fraction(z))
#         poly_frac.append(vertex)
#     return poly_frac


def convert_to_float(poly):
    """convert polygon vertex to float type"""
    poly_float = []
    for x, y, z in poly:
        vertex = (float(x),
                  float(y),
                  float(z))
        poly_float.append(vertex)
    return poly_float


def cross_product(a, b):
    """3-vector product"""
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def dot_product(a, b):
    """scalar product of 3-vectors"""
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vect_diff(a, b):
    """vector difference"""
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def poly_normal(poly):
    """return normal vector for first three vertex"""
    assert len(poly) >= 3
    x, y, z = poly[:3]
    u = vect_diff(y, x)
    v = vect_diff(z, y)
    return cross_product(u, v)


def intersect_list(poly, plain_norm, plain_point, proj_dir):
    """list of intersection points

    find points where the edges enter or leave upper half-space over the plain
    :return list of points projection on proj_dir
    """
    # vertex projection
    u = [dot_product(vert, proj_dir) for vert in poly]

    # plain anchor
    vr = dot_product(plain_point, plain_norm)

    # polygon vertex
    v = [dot_product(vert, plain_norm) for vert in poly]

    u_list = []
    for i in range(len(poly)):
        if (v[i-1] > vr) != (v[i] > vr):
            ur = ((vr - v[i-1]) * u[i] + (v[i] - vr) * u[i-1]) / (v[i] - v[i-1])
            u_list.append(ur)

    return u_list


def points_to_str(a_points, b_points):
    """string representing the order of points 'a' and 'b'"""
    a_pairs = [('a', val) for val in a_points]
    b_pairs = [('b', val) for val in b_points]
    pairs = sorted(a_pairs + b_pairs, key=lambda pair: pair[1])
    letters = [ch for ch, _ in pairs]
    return ''.join(letters)


def recognize_str(s):
    """return True if string s belong to the grammar

    The context-free grammar is given
    S -> SS
    S -> a S a
    S -> b S b
    S -> e

    The recognising automaton is implemented
    """
    toggle = {'a':'b', 'b':'a'}
    cross_num = 0
    top = None
    for ch in s:
        if not cross_num:
            cross_num = 1
            top = ch
            continue

        if ch == top:
            cross_num -= 1
        else:
            cross_num += 1

        if cross_num:
            top = toggle[top]
        else:
            top = None
    return not cross_num


def is_well_connected(a, b):
    """Two planar polygons are bind together in 3D

    Arguments:
        a_poly,
        b_poly -- lists of vertex triples
    """
    a = convert_to_float(a)
    b = convert_to_float(b)

    a_norm = poly_normal(a)
    b_norm = poly_normal(b)

    common_dir = cross_product(a_norm, b_norm)
    if not any(common_dir):
        return False

    a_list = intersect_list(a, b_norm, b[0], common_dir)
    b_list = intersect_list(b, a_norm, a[0], common_dir)

    char_str = points_to_str(a_list, b_list)
    return not recognize_str(char_str)


def run_from_console():
    a_len, = [int(num) for num in input().split()]

    a = []
    for _ in range(a_len):
        vertex = tuple(int(num) for num in input().split())
        a.append(vertex)

    b_len, = [int(num) for num in input().split()]

    b = []
    for _ in range(b_len):
        vertex = tuple(int(num) for num in input().split())
        b.append(vertex)

    if is_well_connected(a, b):
        print('YES')
    else:
        print('NO')


def __starting_point():
    run_from_console()
__starting_point()
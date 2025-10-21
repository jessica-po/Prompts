# python3
import sys


def read_all_following_lines():
    lines = sys.stdin.readlines()
    return (tuple(map(int, line.split())) for line in lines)


class AbcString(object):
    def __init__(self, string):
        self.prefix_bc = [0]
        self.a_strike = [0]

        bc, strike = 0, 0
        for symbol in string:
            if symbol == 'A':
                strike += 1
            else:
                strike = 0
                bc += 1
            self.prefix_bc.append(bc)
            self.a_strike.append(strike)

    def get_info(self, begin, end):
        bc = self.prefix_bc[end] - self.prefix_bc[begin]
        trailing_a = min(self.a_strike[end], end - begin)
        return bc, trailing_a


def can_mutate(start, finish):
    from_bc, from_a = start
    to_bc, to_a = finish

    if (from_bc & 1) != (to_bc & 1): return False
    if from_bc > to_bc: return False
    if from_a < to_a: return False

    if from_bc == to_bc: return (from_a - to_a) % 3 == 0
    if from_a == to_a: return from_bc != 0

    # from_bc < to_bc
    # from_a > to_a
    return True


def main():
    s = AbcString(input())
    t = AbcString(input())
    input()  # skip one line
    requests = read_all_following_lines()

    answer = ""
    for (a, b, c, d) in requests:
        can = can_mutate(s.get_info(a - 1, b), t.get_info(c - 1, d))
        answer += "1" if can else "0"

    print(answer)


main()
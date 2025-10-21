import math
from functools import reduce

url = "https://atcoder.jp//contests/abc070/tasks/abc070_c"

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def main():
    count = int(input())
    clocks = []
    for i in range(count):
        clocks.append(int(input()))
    print((lcm(*clocks)))

def __starting_point():
    main()

__starting_point()
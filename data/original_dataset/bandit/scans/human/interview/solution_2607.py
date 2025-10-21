# @author 

import sys

class ABeautifulString:
    def solve(self):

        def get_not(arr):
            for x in ['a', 'b', 'c']:
                if x not in arr:
                    return x

            assert(False)

        for _ in range(int(input())):
            s = list(input())
            n = len(s)
            for i in range(n - 1):
                if s[i] == s[i + 1] and s[i] != '?':
                    print(-1)
                    break
            else:
                x = 3 * ord('a') + 1 +2
                for i in range(n):
                    if s[i] == '?':
                        if (i > 0 and i < n - 1):
                            s[i] = get_not([s[i - 1], s[i + 1]])
                        elif i == 0:
                            s[i] = get_not([s[i + 1]])
                        else:
                            s[i] = get_not([s[i - 1]])

                print(''.join(s))

solver = ABeautifulString()
input = sys.stdin.readline

solver.solve()
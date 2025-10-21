import sys
class Person:
    def __init__(self, dollars, index):
        self.dollars = dollars
        self.index = index

def solve():
    n = int(input())
    given = list(map(int, input().split()))
    people = list()
    for i in range(n):
        people.append(Person(given[i], i))
    people.sort(key = lambda p: p.dollars + p.index)
    res = [0] * n
    for i in range(n):
        res[i] = people[i].dollars + people[i].index - i
    for i in range(n - 1):
        if res[i] > res[i+1]:
            return ":("
    return ' '.join(map(str, res))

    
def run():
    if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
    print(solve())

run()
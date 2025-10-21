import math
import re
from fractions import Fraction
from collections import Counter

class Task:
    ips = []
    k = 0
    answer = ''
    
    def __init__(self):
        n, self.k = [int(x) for x in input().split()]
        self.ips = ['' for _ in range(n)]
        for i in range(len(self.ips)):
            self.ips[i] = input()

    def solve(self):
        ips, k = self.ips, self.k
        ipAsNumbers = []
        for currentIp in ips:
            number = 0
            parts = currentIp.split('.')
            for i in range(0, len(parts)):
                number += int(parts[i]) * 2**(32 - (i + 1) * 8)
            ipAsNumbers += [number]

        mask = 0
        for i in range(31, -1, -1):
            mask += 2**i
            netAddresses = set()
            for ip in ipAsNumbers:
                netAddresses.add(mask & ip)
            if len(netAddresses) == k:
                mask = bin(mask)[2:]
                self.answer = '.'.join([str(int(mask[i : i + 8], 2)) \
                    for i in range(0, len(mask), 8)])
                return
        self.answer = '-1'


    def printAnswer(self):
        print(self.answer)
        #for line in self.answer:
        #    print(line)

task = Task()
task.solve()
task.printAnswer()
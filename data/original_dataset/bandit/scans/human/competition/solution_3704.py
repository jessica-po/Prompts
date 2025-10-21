#!/usr/bin/env python3
# Copied solution

import collections
import sys
import traceback

class Input(object):
    def __init__(self):
        self.fh = sys.stdin

    def next_line(self):
        while True:
            line = sys.stdin.readline()
            if line == '\n':
                continue
            return line


    def next_line_ints(self):
        line = self.next_line()
        return [int(x) for x in line.split()]

    def next_line_strs(self):
        line = self.next_line()
        return line.split()

class Node(object):
    def __init__(self, color, subtree_color):
        self.left = self.right = None
        self.color = color
        self.subtree_color = subtree_color

def list_to_number(list):
    """Return (color, bits, number)."""
    color = 1 if list[0] == '-' else 2
    values = list[1:].split('/')
    bits = 32
    if len(values) == 2:
        bits = int(values[1])
    nums = values[0].split('.')
    number = 0
    for num in nums:
        number = number * 256 + int(num)
    return (color, bits, number)

def add_list_to_tree(tree, list):
    color, bits, number = list_to_number(list)
    shift = 31
    for _ in range(bits):
        tree.subtree_color |= color
        value = (number >> shift) & 1
        if value == 0:
            if not tree.left:
                tree.left = Node(0, 0)
            tree = tree.left
        else:
            if not tree.right:
                tree.right = Node(0, 0)
            tree = tree.right
        shift -= 1
    tree.subtree_color |= color
    tree.color |= color

def check_tree(tree):
    if not tree:
        return True
    if tree.color == 3 or (tree.color and (tree.subtree_color & ~tree.color)):
        return False
    return check_tree(tree.left) and check_tree(tree.right)

def number_to_list(number, bits):
    number <<= (32 - bits)
    values = []
    for _ in range(4):
        #print('number = {}'.format(number))
        values.append(str(number % 256))
        number //= 256
    values = values[::-1]
    return '.'.join(values) + '/' + str(bits)

def get_optimized(tree, optimized, number, bits):
    if not tree or (tree.subtree_color & 1) == 0:
        return
    if tree.subtree_color == 1:
        list = number_to_list(number, bits)
        #print('number_to_list({}, {}) = {}'.format(number, bits, list))
        optimized.append(list)
        return
    get_optimized(tree.left, optimized, number * 2, bits + 1)
    get_optimized(tree.right, optimized, number * 2 + 1, bits + 1)


def get_optimized_lists(lists):
    tree = Node(0, 0)
    for list in lists:
        add_list_to_tree(tree, list)
    if not check_tree(tree):
        return None
    optimized = []
    get_optimized(tree, optimized, 0, 0)
    return optimized


def main():
    input = Input()
    while True:
        try:
            nums = input.next_line_ints()
            if not nums:
                break
            n, = nums
            if n == -1:
                break
            lists = []
            for _ in range(n):
                lists.append(input.next_line_strs()[0])
        except:
            print('read input failed')
        try:
            optimized = get_optimized_lists(lists)
            if optimized is None:
                print("-1")
            else:
                print("{}".format(len(optimized)))
                for l in optimized:
                    print("{}".format(l))
        except:
            traceback.print_exc(file=sys.stdout)
            print('get_min_dist failed')

main()
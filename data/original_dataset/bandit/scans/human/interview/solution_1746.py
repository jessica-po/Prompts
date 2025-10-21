#!/usr/bin/env python3

def main():
    class Node:
        def __init__(self):
            self.children = [ ]

    n = int(input())
    nodes = [Node() for i in range(n)]
    for i in range(1, n):
        p = int(input())
        nodes[p - 1].children.append(nodes[i])
    ok = all(
        len([child for child in node.children if not child.children]) >= 3
        for node in nodes
        if node.children
    )
    print("Yes" if ok else "No")

try:
    while True:
        main()
except EOFError:
    pass
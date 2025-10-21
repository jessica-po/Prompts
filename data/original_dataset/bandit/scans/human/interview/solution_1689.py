#!/usr/bin/env python3

def main():
    try:
        while True:
            n = int(input())
            grid = [input() for i in range(n)]
            for i, row in enumerate(grid):
                if row[:2] == "OO":
                    grid[i] = "++" + row[2:]
                    break
                elif row[-2:] == "OO":
                    grid[i] = row[:-2] + "++"
                    break
            else:
                print("NO")
                continue

            print("YES")
            print('\n'.join(grid))

    except EOFError:
        pass

main()
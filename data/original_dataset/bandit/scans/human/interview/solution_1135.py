#!/usr/bin/env python3

def main():
    try:
        while True:
            n = int(input())
            s = input()
            result = ""
            for m, c in enumerate(reversed(s)):
                result = result[:m >> 1] + c + result[m >> 1:]

            print(result)

    except EOFError:
        pass

main()
# -*- coding: utf-8 -*-

ngoods = {
    '0': 2,
    '1': 7,
    '2': 2,
    '3': 3,
    '4': 3,
    '5': 4,
    '6': 2,
    '7': 5,
    '8': 1,
    '9': 2
}

digits = input().strip()
print(ngoods[digits[0]] * ngoods[digits[1]])
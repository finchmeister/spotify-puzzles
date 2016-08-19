# Reverse Binary Puzzle
# https://labs.spotify.com/puzzles/
# jfinch

import sys


def get_max_2_exp(decimal, exp=0):
    if 2**exp <= decimal:
        return get_max_2_exp(decimal, exp + 1)
    else:
        return exp-1


def decimal_to_binary(decimal):
    binary_dict = {}
    while True:
        exp = get_max_2_exp(decimal)
        decimal -= 2 ** exp
        binary_dict[exp] = 1
        if decimal < 0:
            break
    binary = ''
    for i in range(max(binary_dict.keys()), -1, -1):
        if binary_dict.get(i):
            binary += '1'
        else:
            binary += '0'
    return binary


def binary_to_decimal(binary):
    decimal, exp = 0, 0
    for x in binary[::-1]:
        y = int(x)
        decimal += y*2**exp
        exp += 1
    return decimal


def reverse_binary(decimal):
    binary = decimal_to_binary(decimal)
    reversed_binary = binary[::-1]
    return binary_to_decimal(reversed_binary)


decimal = int(sys.stdin.readline())
print(reverse_binary(decimal))
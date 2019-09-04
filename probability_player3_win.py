# -*- coding: utf-8 -*-

from math import gcd


def main():
    
    a = input('Enter Player A dice value: ')
    b = input('Enter Player A dice value: ')

    Probability(int(a), int(b))


def Probability(a, b) :

    c = 6 - max(a, b)

    __gcd = gcd(c, 6)

    print(c // __gcd, "/", 6 // __gcd)


if __name__ == "__main__":
    main()

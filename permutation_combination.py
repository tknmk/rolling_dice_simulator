# -*- coding: utf-8 -*-
from itertools import permutations
from itertools import combinations
import math


def main():

    # 順列
    permutation()
    print(permutation_nums(3, 2))

    # 組み合わせ
    combination()
    print(combination_num(3, 2))


def permutation():
    """
    ### 順列
    @return
    [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
    """
    result = permutations("abc", 2)
    print(list(result))
    


def combination():
    """
    ### 組み合わせ
    @return
    [('a', 'b'), ('a', 'c'), ('b', 'c')]
    """
    result = combinations("abc", 2)
    print(list(result))


def permutation_nums(e, c):

    """
    ### 順列
    要素を指定して、順列する要素の数を返す
    """
    return math.factorial(e)//math.factorial(e-c)


def combination_num(e, c):
    """
    ### 組み合わせ
    要素を指定して、順列する要素の数を返す
    """
    return permutation_nums(e, c)//math.factorial(c)


if __name__ == "__main__":
    main()


# -*- coding: utf-8 -*-
import random

def main():

    # バブルソート
    print('#### バブルソート ####')
    result_b = bubble_sort()
    print('Result: {0}'.format(result_b))

    # クイックソート
    print('#### クイックソート ####')
    result_q = quick_sort(random_nums(10))
    print('Result: {0}'.format(result_q))


def random_nums(num):

    nums = list(range(num))
    random.shuffle(nums)
    return nums


def bubble_sort():
    """
    ### バブルソート
    (x ≦ y < z)
    n個の要素があったとして、必ず"n(n-1)/2"回のスキャンが実行される。
    要素の数が多くなるほど、実行速度は遅くなる。
    """
    # 要素の数を決定
    nums = list(range(15))
    random.shuffle(nums)
    print('Random Numbers : {0}'.format(nums))
    
    # Sort
    for index in range(len(nums)-1, 0, -1):
        for l in range(index):
            if nums[l] > nums[l+1]:
                tmp = nums[l+1]
                nums[l+1] = nums[l]
                nums[l] = tmp

    return nums


def quick_sort(nums):
    """
    ### クイックソート
    (x ≦ y < z)
    基点(y)を軸に。分割を繰り返して整列を行う。
    """
    print('Random Numbers : {0}'.format(nums))
    less = []
    greater = []
    equal = []

    if len(nums) > 1:
        pivot = nums[0]

        for x in nums:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return nums



if __name__ == "__main__":
    main()



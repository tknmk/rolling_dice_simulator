# -*- coding: utf-8 -*-


def main():

    lst = [1, 3, 5, 9, 18, 20]
    target = 1

    # Binary Search
    bs_result = binary_search(0, len(lst)-1, lst, target)
    if bs_result != -1:
        print(f'ターゲット {target} は、{bs_result+1} 番目に見つかりました!!')
    else:
        print(f'ターゲット {target} は、見つかりませんでした。')


def binary_search(l, h, lst, target):
    """
    ### 二分探索(Binary Search)
    ソート済みのリストや配列に入ったデータに対する検索を行う。
    この時、同一の値はないものとし、中央の値をみて検索したい値との大小を関係をみる。
    n個のデータの中央値を見て、奇数(n-1)/2個、偶数n/2の要素を無視できる。
    """
    print(f'ターゲット: {target}')

    mid = l + (h-1)/2

    while l <= h:

        mid = (l + h) // 2 
        print(f'### log 中央値: {mid}')

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            l = mid + 1
        else:
            h = mid - 1

    return -1


if __name__ == "__main__":
    main()


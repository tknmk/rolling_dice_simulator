# -*- coding: utf-8 -*-
"""
### アナグラム
文字列が全く同じということを前提に、
文字列をソートし、比較します。
@return boolean
"""
def main():
   
    lst_a = 'abcde'
    lst_b = 'edcba'
    print(sort_compare(lst_a, lst_b))


def sort_compare(lst_a, lst_b):

    a_list = list(lst_a)
    b_list = list(lst_b)

    a_list.sort()
    b_list.sort()

    pos = 0
    matches = True

    while pos < len(lst_a) and matches:
        if a_list[pos]==b_list[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


if __name__ == "__main__":
    main()





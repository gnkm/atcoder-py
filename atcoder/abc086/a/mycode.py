"""ABC086A - Product
[AtCoder Beginners Selection]

シカのAtCoDeerくんは二つの正整数 a,b を見つけました。 a と b の積が偶数か奇数か判定してください。
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    a, b = map(int, input())
    if a % 2 == 0 or b % 2 == 0:
        print('Even')
    else:
        print('Odd')


if __name__ == '__main__':
    main()

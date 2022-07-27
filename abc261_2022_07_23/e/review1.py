"""E - Many Operations
YouTube の解説動画内の回答

問題
https://atcoder.jp/contests/abc261/tasks/abc261_e

解説動画
https://www.youtube.com/watch?v=P20UCEOnUzU&t=7720s
"""

import icecream, pprint  # for debugging
import sys


_input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, _input()))          # input multi element single line int

sys.setrecursionlimit(1000000)


def main():
    # print_bit_operation()
    # test_operators()
    # print_sample1()
    # print_sample2()
    # sys.exit()

    N, C = i_mesli()
    operations = [tuple(map(int, input().split())) for _ in range(N)]

    d = [1, ~0]
    for t, a in operations:
        for j in range(2):
            if t == 1:
                d[j] &= a
            elif t == 2:
                d[j] |= a
            else:
                d[j] ^= a

        C = (C & d[1]) | (~C & d[0])
        print(C)

    sys.exit()


def test_operators() -> None:
    pass


def print_bit_operation() -> None:
    icecream.ic(~0)          # ic| ~0: -1
    icecream.ic(~0 & 0)      # ic| ~0 & 0: 0
    icecream.ic(~0 & 1)      # ic| ~0 & 1: 1
    icecream.ic(~0 | 0)      # ic| ~0 | 0: -1
    icecream.ic(~0 | 1)      # ic| ~0 | 1: -1
    icecream.ic(~0 ^ 0)      # ic| ~0 ^ 0: -1
    icecream.ic(~0 ^ 1)      # ic| ~0 ^ 1: -2
    icecream.ic(6 & 0)       # ic| 6 & 0: 0
    icecream.ic(6 & 1)       # ic| 6 & 1: 0
    icecream.ic(6 | 0)       # ic| 6 | 0: 6
    icecream.ic(6 | 1)       # ic| 6 | 1: 7
    icecream.ic(6 ^ 0)       # ic| 6 ^ 0: 6
    icecream.ic(6 ^ 1)       # ic| 6 ^ 1: 7
    icecream.ic(bin(6))      # ic| bin(6): '0b110'
    icecream.ic(bin(6 & 0))  # ic| bin(6 & 0): '0b0'
    icecream.ic(bin(6 & 1))  # ic| bin(6 & 1): '0b0'
    icecream.ic(bin(6 | 0))  # ic| bin(6 | 0): '0b110'
    icecream.ic(bin(6 | 1))  # ic| bin(6 | 1): '0b111'
    icecream.ic(bin(6 ^ 0))  # ic| bin(6 ^ 0): '0b110'
    icecream.ic(bin(6 ^ 1))  # ic| bin(6 ^ 1): '0b111'


def print_sample1() -> None:
    x0 = 10
    a1 = 3   # operator: ^
    a2 = 5   # operator: |

    expected1 = 9
    expected2 = 15

    x1 = operation_and(x0, a1)
    assert x1 == expected1, f'actuary: {x1}, expected: {expected1}'  # => OK
    x2 = operation_or(
        operation_xor(x1, a2),
        a2
    )
    assert x2 == expected2, f'actuary: {x2}, expected: {expected2}'  # => AssertionError: actuary: 13, expected: 15


def print_sample2() -> None:
    x0 = 10
    a1 = 3   # operator: ^
    a2 = 5   # operator: |
    a3 = 12  # operator: &

    expected1 = 9
    expected2 = 15
    expected3 = 12

    x1 = operation_and(x0, a1)
    assert x1 == expected1, f'actuary: {x1}, expected: {expected1}'  # => OK
    x2 = operation_or(
        operation_xor(x1, a2),
        a2
    )
    assert x2 == expected2, f'actuary: {x2}, expected: {expected2}'  # => AssertionError: actuary: 13, expected: 15


def operation_and(x, a):
    return x & a


def operation_or(x, a):
    return x | a


def operation_xor(x, a):
    return x ^ a


if __name__ == '__main__':
    main()

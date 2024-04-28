"""A - The bottom of the ninth
https://atcoder.jp/contests/abc351/tasks/abc351_a

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    heads = i_mesli()
    tails = i_mesli()
    head_point = sum(heads)
    tail_point = sum(tails)
    print(head_point - tail_point + 1)
    sys.exit()


if __name__ == "__main__":
    main()

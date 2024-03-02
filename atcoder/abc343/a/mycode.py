"""A - Wrong Answer
https://atcoder.jp/contests/abc343/tasks/abc343_a

Problem statement here.
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    A, B = i_mesli()
    correct = A + B
    if 0 <= correct - 1 <= 9:
        print(correct - 1)
    else:
        print(correct + 1)
    sys.exit()


if __name__ == "__main__":
    main()

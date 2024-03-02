"""C - 343
https://atcoder.jp/contests/abc343/tasks/abc343_c

Problem statement here.
"""

import math
import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int


def main():
    N = i_sesli()
    # for n in range(N, 0, -math.floor(pow(N, 1 / 3))):
    for n in range(N, 0, -1):
        print(f"{n = }, {is_cubic(n) = }, {is_palindrome(n)}")
        if is_cubic(n) and is_palindrome(n):
            print(n)
            break
    sys.exit()


def is_cubic(n):
    for x in range(math.ceil(pow(n, 1 / 3)), 0, -1):
        if n == pow(x, 3):
            return True
    return False


def is_palindrome(n):
    num_str = list(str(n))
    for i, s in enumerate(num_str):
        if s != num_str[-i - 1]:
            return False
    return True


if __name__ == "__main__":
    main()

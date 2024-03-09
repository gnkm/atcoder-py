"""C - A+B+C
https://atcoder.jp/contests/abc344/tasks/abc344_c

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N = i_sesli()
    seq_A = i_mesli()
    M = i_sesli()
    seq_B = i_mesli()
    L = i_sesli()
    seq_C = i_mesli()
    Q = i_sesli()
    seq_X = i_mesli()
    nums = set()
    for a in seq_A:
        for b in seq_B:
            for c in seq_C:
                nums.add(a + b + c)

    for x in seq_X:
        if x in nums:
            print("Yes")
        else:
            print("No")

    sys.exit()


if __name__ == "__main__":
    main()

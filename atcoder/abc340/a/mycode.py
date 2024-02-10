"""A - Arithmetic Progression
https://atcoder.jp/contests/abc340/tasks/abc340_a
"""

# for debugging
import pprint
# Scripts starts here.
import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    A, B, D = i_mesli()
    seq = [str(x) for x in range(A, B + 1, D)]
    # print(" ".join(seq))
    print(*seq)
    sys.exit()


if __name__ == "__main__":
    main()

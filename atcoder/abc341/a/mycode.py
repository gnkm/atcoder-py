"""A - Print 341
https://atcoder.jp/contests/abc341/tasks/abc341_a

Result: AC
"""
import sys


def main():
    N = int(input())
    ones = list("1" * (N + 1))
    print("0".join(ones))
    sys.exit()


if __name__ == "__main__":
    main()

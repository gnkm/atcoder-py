"""A - Past ABCs
https://atcoder.jp/contests/abc350/tasks/abc350_a

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    S = input()
    exists = [f"ABC{i:03}" for i in range(1, 350)]
    exists.remove("ABC316")
    if S in exists:
        print("Yes")
    else:
        print("No")
    sys.exit()


if __name__ == "__main__":
    main()

"""B - Substring
https://atcoder.jp/contests/abc347/tasks/abc347_b

Result: AC
"""

import sys


def main():
    S = input()
    substrings = set()
    size = len(S)
    for i in range(size):
        for j in range(i + 1, size + 1):
            # print(f"{i = }, {j = }, {S[i:j] = }")
            substrings.add(S[i:j])
    print(len(substrings))
    sys.exit()


if __name__ == "__main__":
    main()

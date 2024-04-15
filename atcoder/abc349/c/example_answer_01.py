"""C - Airport Code
https://atcoder.jp/contests/abc349/tasks/abc349_c
https://atcoder.jp/contests/abc349/submissions/52256215

Result: AC
"""

import re
import sys


def main():
    S = input().upper() + "X"
    T = input()
    print("Yes" if re.search(".*".join(T), S) else "No")
    sys.exit()


if __name__ == "__main__":
    main()

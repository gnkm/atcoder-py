"""Title

URL

Problem statement here.
"""

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesls = lambda: str(input()[0])  # input single element single line str


def main():
    s = i_sesls()
    counter = Counter(s)
    single_letter = [k for k, v in counter.items() if v == 1][0]
    print(s.find(single_letter) + 1)
    sys.exit()


if __name__ == "__main__":
    main()

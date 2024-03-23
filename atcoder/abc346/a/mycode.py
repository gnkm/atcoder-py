"""Title

URL

Problem statement here.
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N = i_sesli()
    numbers = i_mesli()
    seq_B = []
    for i, a in enumerate(numbers):
        if i == len(numbers) - 1:
            break
        seq_B.append(str(a * numbers[i + 1]))
    print(" ".join(seq_B))
    sys.exit()


if __name__ == "__main__":
    main()

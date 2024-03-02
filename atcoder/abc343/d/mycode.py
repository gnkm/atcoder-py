"""D - Diversity of Scores
https://atcoder.jp/contests/abc343/tasks/abc343_d

Problem statement here.
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N, T = i_mesli()
    variances = i_memli(T)
    scores = {str(n): 0 for n in range(1, N + 1)}

    for v in variances:
        scores[str(v[0])] += v[1]
        # print(scores)
        _set = set(scores.values())
        print(len(_set))
    sys.exit()


if __name__ == "__main__":
    main()

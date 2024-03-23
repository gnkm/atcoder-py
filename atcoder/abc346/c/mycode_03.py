"""C - Σ
https://atcoder.jp/contests/abc346/tasks/abc346_c

長さ N の正整数列 A=(A1,A2,…,AN) および正整数 K が与えられます。
1 以上 K 以下の整数のうち、A の中に一度も現れないものの総和を求めてください。

Result: TLE, MLE, RE
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N, K = i_mesli()
    seq_A_org = i_mesli()
    sum_A = sum(set([num for num in seq_A_org if num <= K]))
    print(sum([i for i in range(1, K + 1)]) - sum_A)
    sys.exit()


if __name__ == "__main__":
    main()

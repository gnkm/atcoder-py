"""C - Σ
https://atcoder.jp/contests/abc346/tasks/abc346_c

長さ N の正整数列 A=(A1,A2,…,AN) および正整数 K が与えられます。
1 以上 K 以下の整数のうち、A の中に一度も現れないものの総和を求めてください。

Result: TLE
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N, K = i_mesli()
    seq_A = i_mesli()
    set_A = set(seq_A)
    set_K = set([i for i in range(1, K + 1)])
    not_in_A = set_K - set_A
    print(sum(not_in_A))
    sys.exit()


if __name__ == "__main__":
    main()

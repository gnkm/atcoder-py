"""C - Σ
https://atcoder.jp/contests/abc346/tasks/abc346_c
https://atcoder.jp/contests/abc346/editorial/9635

長さ N の正整数列 A=(A1,A2,…,AN) および正整数 K が与えられます。
1 以上 K 以下の整数のうち、A の中に一度も現れないものの総和を求めてください。

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N, K = i_mesli()
    seq_A_org = i_mesli()
    seq_A = set(seq_A_org)
    ans = K * (K + 1) // 2
    for num in seq_A:
        if num <= K:
            ans -= num

    print(ans)
    sys.exit()


if __name__ == "__main__":
    main()

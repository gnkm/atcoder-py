"""C - Many Replacement
https://atcoder.jp/contests/abc342/tasks/abc342_c

英小文字からなる長さ N の文字列 S が与えられます。
文字列 S に対して操作を Q 回行います。

制約
- 1 ≤ N ≤ 2 × 10^5
- 1 ≤ Q ≤ 2 × 10^5

`str.translate()` を使うことで、計算量を O(26*(N + Q)) にできる。

Results: AC
"""

import sys
from string import ascii_lowercase

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_sesls = lambda: str(input()[0])  # input single element single line str
i_mesls = lambda: list(input())  # input multi element single line str
i_memls = lambda n: [i_mesls() for _ in range(n)]  # input multi element multi line str


def main():
    N = i_sesli()
    S = i_sesls()
    Q = i_sesli()
    queries = i_memls(Q)
    mapping_from = ascii_lowercase
    mapping_to = ascii_lowercase
    for query in queries:
        mapping_to = mapping_to.replace(query[0], query[1])
    print(S.translate(str.maketrans(mapping_from, mapping_to)))
    sys.exit()


if __name__ == "__main__":
    main()

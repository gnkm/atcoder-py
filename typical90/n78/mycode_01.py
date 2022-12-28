"""078 - Easy Graph Problem（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_bz

N 頂点 M 辺の連結な単純無向グラフが与えられます。グラフの頂点には、それぞれ 1 から N までの番号が振られています。 i 番目の辺は、頂点 a_i と b_i を双方向に結んでいます。

以下の条件を満たす頂点の個数はいくつあるか出力してください。

- 自分自身より頂点番号が小さい隣接頂点がちょうど 1 つ存在する
"""

# for debugging
import pkg_resources

if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic
else:
    debug = print

import pprint

# Scripts starts here.
import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: mapl(int, input())               # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N, M = map(int, input())
    edges = i_memli(M)
    node_numbers = {i: set() for i in range(1, N + 1)}
    for edge in edges:
        smaller_node = min(edge)
        larger_node = max(edge)
        node_numbers[larger_node].add(smaller_node)

    print(len([True for k, v in node_numbers.items() if len(v) == 1]))
    sys.exit()


if __name__ == '__main__':
    main()

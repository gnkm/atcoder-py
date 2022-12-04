"""033 - Not Too Bright（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_ag

E869120 くんは、冬に公開するイルミネーションを作成することを計画しています。
E869120 くんが計画しているイルミネーションは、縦 H × 横 W の HW 個のLEDで構成されます。
イルミネーションの各 LED は、点灯・消灯の状態を任意に切り替えることができます。

このイルミネーションは、以下の条件を満たすとき 不適切である といいます。

- イルミネーション全体に完全に含まれる 縦 2 × 横 2 の、4 つの LED を含む領域であって、点灯している LED が領域内に 2 つ以上あるものが存在する。

適切な（不適切な状態ではない）イルミネーションの点灯パターンのうち、点灯している LED の個数としてありうる最大値を求めてください。

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
import math
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    H, W = map(int, input())
    if H == 1 or W == 1:
        print(H * W)
    else:
        print(math.ceil(H / 2) * math.ceil(W / 2))

    sys.exit()


if __name__ == '__main__':
    main()

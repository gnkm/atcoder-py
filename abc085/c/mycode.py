"""ABC085C - Otoshidama

日本でよく使われる紙幣は、10000 円札、5000 円札、1000 円札です。以下、「お札」とはこれらのみを指します。

青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N 枚入っていて、合計で Y 円だったそうですが、嘘かもしれません。このような状況がありうるか判定し、ありうる場合はお年玉袋の中身の候補を一つ見つけてください。なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。

70 ms
64816 KB
"""

# for debugging
import icecream
debug = icecream.ic
import pprint

# Scripts starts here.
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: map(int, input())               # input multi element single line int


def main():
    N, Y = i_mesli()
    for i in range(N + 1):
        x = i
        for j in range(N + 1 - i):
            y = j
            z = N - x - y
            if 10_000 * x + 5_000 * y + 1_000 * z == Y:
                print(f'{x} {y} {z}')
                sys.exit()

    print('-1 -1 -1')
    sys.exit()


if __name__ == '__main__':
    main()

"""ABC085C - Otoshidama

日本でよく使われる紙幣は、10000 円札、5000 円札、1000 円札です。以下、「お札」とはこれらのみを指します。

青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N 枚入っていて、合計で Y 円だったそうですが、嘘かもしれません。このような状況がありうるか判定し、ありうる場合はお年玉袋の中身の候補を一つ見つけてください。なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。

参考
https://atcoder.jp/contests/abs/submissions/2202564

65 ms
63912 KB
"""

# for debugging
import icecream
debug = icecream.ic
import pprint

# Scripts starts here.
import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    N, Y = map(int, input())
    Y_d1000 = Y // 1000
    x_max = (Y_d1000 - N) // 9

    if x_max < 0:
        print('-1 -1 -1')
        sys.exit()

    for x_candidate in range(x_max + 1):
        if (Y_d1000 - N - 9 * x_candidate) % 4 != 0:
            continue

        y_candidate = (Y_d1000 - N - 9 * x_candidate) // 4
        z_candidate = N - x_candidate - y_candidate
        if z_candidate < 0:
            continue

        print(f'{x_candidate} {y_candidate} {z_candidate}')
        sys.exit()

    print('-1 -1 -1')
    sys.exit()


if __name__ == '__main__':
    main()

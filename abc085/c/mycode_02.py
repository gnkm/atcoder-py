"""ABC085C - Otoshidama

日本でよく使われる紙幣は、10000 円札、5000 円札、1000 円札です。以下、「お札」とはこれらのみを指します。

青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N 枚入っていて、合計で Y 円だったそうですが、嘘かもしれません。このような状況がありうるか判定し、ありうる場合はお年玉袋の中身の候補を一つ見つけてください。なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。

Memo

公式解説で計算量が O(N) となる方法として紹介されていたので実装した。
https://www.youtube.com/watch?v=-QHM9Dk9hRw&t=2850s

183 ms
62820 KB
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

    z_max = (10 * N - Y_d1000) // 9
    if z_max < 0:
        print('-1 -1 -1')
        sys.exit()

    for z_candidate in range(max(0, (5 * N - Y_d1000) // 5), z_max + 1):
        if (z_candidate - Y_d1000) % 5 != 0:
            continue
        if 5 * N - Y_d1000 > 4 * z_candidate:
            continue
        if 9 * z_candidate > 10 * N - Y_d1000:
            continue

        z = z_candidate
        for x_candidate in range(N - z + 1):
            if 10 * x_candidate + 5 * (N - z - x_candidate) == Y_d1000 - z:
                x = x_candidate
                y = N - x - z
                print(f'{x} {y} {z}')
                sys.exit()

    print('-1 -1 -1')
    sys.exit()


if __name__ == '__main__':
    main()

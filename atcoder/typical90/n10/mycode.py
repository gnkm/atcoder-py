"""010 - Score Sum Queries（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_j

ABC 大学には N 人の一年生が在籍しています。クラスは 2 つあり、学籍番号 i 番の生徒のクラスは C_i 組です。今日は期末試験が返却され、学籍番号 i 番の生徒の点数は P_i 点でした。
以下の形式の質問が Q 個与えられます。j=1,2,…,Q それぞれについて答えてください。

- 学籍番号 L_j - R_j 番の 1 組生徒における、期末試験点数の合計
- 学籍番号 L_j - R_j 番の 2 組生徒における、期末試験点数の合計
- これら 2 つの値をそれぞれ求めよ。

Result: AC
実行時間 289 ms(制限 2000 ms)

累積和を使用。
下記のように定義すると 2200 ms 程かかる。
cumulative_sum1 = [sum([p[1] for p in points[:i] if p[0] == 1]) for i in range(len(points) + 1)]
"""

# for debugging
import icecream
debug = icecream.ic

import pprint

# Scripts starts here.
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: mapl(int, input())
i_memli = lambda n: [i_mesli() for _ in range(n)]


def main():
    N = i_sesli()
    points = i_memli(N)
    Q = i_sesli()
    queries = i_memli(Q)

    cumulative_sum1 = [0]
    cumulative_sum2 = [0]
    acc1 = 0
    acc2 = 0
    for p in points:
        if p[0] == 1:
            acc1 += p[1]
        else:
            acc2 += p[1]

        cumulative_sum1.append(acc1)
        cumulative_sum2.append(acc2)

    for q in queries:
        sum1 = cumulative_sum1[q[1]] - cumulative_sum1[q[0] - 1]
        sum2 = cumulative_sum2[q[1]] - cumulative_sum2[q[0] - 1]
        print(sum1, sum2)

    sys.exit()


if __name__ == '__main__':
    main()

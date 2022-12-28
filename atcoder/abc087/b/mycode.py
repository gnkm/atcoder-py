"""ABC087B - Coins
[AtCoder Beginners Selection]

あなたは、500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。 これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りありますか。
同じ種類の硬貨どうしは区別できません。2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。

入力は以下の形式で標準入力から与えられる。

```
A
B
C
X
```

https://atcoder.jp/contests/abs/tasks/abc087_b
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
from itertools import product
from operator import mul
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int

sys.setrecursionlimit(1000000)


COINS = (500, 100, 50)


def main():
    num_500 = i_sesli()
    num_100 = i_sesli()
    num_050 = i_sesli()
    target_sum_cost = i_sesli()
    candidates = product(
        [i for i in range(num_500 + 1)],
        [i for i in range(num_100 + 1)],
        [i for i in range(num_050 + 1)],
    )
    ans = 0
    for c in candidates:
        sum_cost = sum(map(mul, COINS, c))
        if sum_cost == target_sum_cost:
            ans += 1

    print(ans)
    sys.exit()

if __name__ == '__main__':
    main()

"""
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


import copy
import sys
from time import sleep

import icecream


COINS = [500, 100, 50]


def main():
    inputs = [int(input()) for i in range(len(COINS) + 1)]
    nums = inputs[:3]
    sum_cost = inputs[-1]
    coin_num_dict = dict(zip(COINS, nums))

    print(count_patterns(coin_num_dict, sum_cost))


def count_patterns(coin_num_dict, sum_cost):
    """Return pattern number.

    Args:
        coin_num_dict (Dict[int, int]): {coin: num, ...}
        sum_cost (int): [description]

    Returns:
        int: pattern num
    """
    coin_nums = list(coin_num_dict.values())

    if sum_cost == 0:
        return 1

    if sum(coin_nums) == 0:
        return 0

    if sum_cost < 0:
        return 0

    if sum([coin * num for coin, num in coin_num_dict.items()]) < sum_cost:
        return 0

    pattern_num = 0
    for coin, num in coin_num_dict.items():
        for used_num in range(num):
            _coin_num_dict = copy.deepcopy(coin_num_dict)
            _coin_num_dict[coin] = used_num
            pattern_num += count_patterns(_coin_num_dict, sum_cost - coin * used_num,)

    return pattern_num


if __name__ == '__main__':
    main()

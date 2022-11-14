"""ABC081B - Shift only
[AtCoder Beginners Selection]

黒板に N 個の正の整数 A_1,...,A_N が書かれています．
すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．

- 黒板に書かれている整数すべてを，2 で割ったものに置き換える．

すぬけ君は最大で何回操作を行うことができるかを求めてください．
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    _ = i_sesli()
    nums = i_mesli()
    cnt = 0

    while True:
        if any(list(map(lambda x: x % 2 == 1, nums))):
            break
        else:
            nums = list(map(lambda x: round(x / 2), nums))
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()

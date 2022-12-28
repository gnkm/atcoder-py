"""ABC081A - Placing Marbles
[AtCoder Beginners Selection]

すぬけ君は 1,2,3 の番号がついた 3 つのマスからなるマス目を持っています。 各マスには 0 か 1 が書かれており、マス i には s_i が書かれています。
すぬけ君は 1 が書かれたマスにビー玉を置きます。 ビー玉が置かれるマスがいくつあるか求めてください。
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    nums = list(map(int, list(input()[0])))
    print(sum(nums))


if __name__ == '__main__':
    main()

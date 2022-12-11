"""067 - Base 8 to 9（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_bo

黒板に 8 進法の整数 N が書かれています。あなたは以下の操作を K 回行います。

- 黒板の整数を 9 進法に直し、ここに現れる数字「 8 」を「 5 」に書き直す（書き直した後の数は 8 進数とみなされる）

操作を K 回行った後にできる数を 8 進法で出力してください。

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


input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    N, K = map(int, input())
    base_9_num = N
    for _ in range(K):
        base_9_num = transform(base_9_num, 8, 9)
        base_9_num = int(str(base_9_num).replace('8', '5'))

    print(base_9_num)
    sys.exit()


def transform(number, base_from, base_to):
    if number == 0:
        return 0

    number_decimal = 0
    for i, digit in enumerate(list(map(int, str(number)))[::-1]):
        number_decimal += digit * base_from ** i

    max_dimension = math.floor(math.log(number_decimal, base_to))
    ret_str = ''
    divided_number = number_decimal
    for dimension in range(max_dimension, -1, -1):
        digit = divided_number // base_to ** dimension
        ret_str += str(digit)
        divided_number -= digit * base_to ** dimension

    return int(ret_str)


if __name__ == '__main__':
    main()

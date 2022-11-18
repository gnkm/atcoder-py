"""ABC088B - Card Game for Two

N 枚のカードがあります. i 枚目のカードには, a_i という数が書かれています.
Alice と Bob は, これらのカードを使ってゲームを行います. ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます. Alice が先にカードを取ります.
2 人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります. 2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.
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
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int
i_mesli = lambda: mapl(int, input())               # input multi element single line int

sys.setrecursionlimit(1000000)
INF = float('inf')


def main():
    _ = i_sesli()
    cards = i_mesli()
    sorted_cards = sorted(cards, reverse=True)
    alice = sum([c for i, c in enumerate(sorted_cards) if i % 2 == 0])
    bob = sum([c for i, c in enumerate(sorted_cards) if i % 2 == 1])
    print(alice - bob)
    sys.exit()


if __name__ == '__main__':
    main()

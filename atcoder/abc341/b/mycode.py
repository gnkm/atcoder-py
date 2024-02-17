"""B - Foreign Exchange
https://atcoder.jp/contests/abc341/tasks/abc341_b

Result: AC
"""
# Scripts starts here.
import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))
input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N = i_sesli()
    moneys_init = i_mesli()
    moneys = moneys_init
    rates = i_memli(N - 1)
    for i, _ in enumerate(moneys_init):
        if i == len(moneys_init) - 1:
            break
        exchange = moneys[i] // rates[i][0]
        moneys[i] -= exchange * rates[i][0]
        moneys[i + 1] += exchange * rates[i][1]
    print(moneys[-1])
    sys.exit()


if __name__ == "__main__":
    main()

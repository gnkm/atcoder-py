"""C - Colorful Beans
https://atcoder.jp/contests/abc348/tasks/abc348_c
https://atcoder.jp/contests/abc348/submissions/52062942

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N = i_sesli()
    beans = i_memli(N)
    deliciouses = dict()
    for bean in beans:
        deliciouse = bean[0]
        color = bean[1]
        deliciouses[color] = min(deliciouse, deliciouses.get(color, deliciouse))
    print(max([v for v in deliciouses.values()]))
    sys.exit()


if __name__ == "__main__":
    main()

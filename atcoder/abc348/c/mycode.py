"""C - Colorful Beans
https://atcoder.jp/contests/abc348/tasks/abc348_c

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
    # values[color] = min_deliciousness
    # max(values[color]) となる color が回答
    colors = set([e[1] for e in beans])
    values = {c: 10**10 for c in colors}
    for row in beans:
        if row[0] < values[row[1]]:
            values[row[1]] = row[0]
    # print(f"{values = }")
    max_value = 0
    for d in values.values():
        max_value = max(d, max_value)
    print(max_value)
    sys.exit()


if __name__ == "__main__":
    main()

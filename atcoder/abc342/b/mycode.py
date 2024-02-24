"""Title

URL

Problem statement here.
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N = i_sesli()
    persons = i_mesli()
    Q = i_sesli()
    queries = i_memli(Q)
    for query in queries:
        a = query[0]
        b = query[1]
        for p in persons:
            if p == a:
                print(a)
                break
            elif p == b:
                print(b)
                break
            else:
                continue
    sys.exit()


if __name__ == "__main__":
    main()

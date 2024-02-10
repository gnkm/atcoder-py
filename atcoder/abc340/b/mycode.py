"""B - Append
https://atcoder.jp/contests/abc340/tasks/abc340_b
"""

# for debugging
import pkg_resources

if any([str(i).startswith("icecream") for i in pkg_resources.working_set]):
    import icecream

    debug = icecream.ic
else:
    debug = print

import pprint
# Scripts starts here.
import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    Q = i_sesli()
    queries = i_memli(Q)
    seq = []
    for query_type, num in queries:
        if query_type == 1:
            seq.append(num)
        else:
            print(seq[-num])

    sys.exit()


if __name__ == "__main__":
    main()

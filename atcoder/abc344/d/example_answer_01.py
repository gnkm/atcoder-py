"""D - String Bags
https://atcoder.jp/contests/abc344/tasks/abc344_d

https://atcoder.jp/contests/abc344/submissions/51029984

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesls = lambda: str(input()[0])  # input single element single line str
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesls = lambda: list(input())  # input multi element single line str
i_memls = lambda n: [i_mesls() for _ in range(n)]  # input multi element multi line str


def main():
    T = i_sesls()
    N = i_sesli()
    bags_org = i_memls(N)
    bags = mapl(lambda x: x[1:], bags_org)
    dp = {"": 0}
    for bag in bags:
        dp_copy = dp.copy()
        for substr, cost in dp.items():
            for str_in_bag in bag:
                if T.startswith(substr + str_in_bag):
                    dp_copy[substr + str_in_bag] = min(
                        dp_copy.get(substr + str_in_bag, 10**18), cost + 1
                    )
        dp = dp_copy

    print(dp.get(T, -1))
    sys.exit()


if __name__ == "__main__":
    main()

"""E - Set Add Query
https://atcoder.jp/contests/abc347/tasks/abc347_e

Result: TLE
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    N, Q = map(int, input().split())
    queries = mapl(int, input().split())
    A = [0 for i in range(N)]
    S = set()
    for query_num in queries:
        if query_num in S:
            S.remove(query_num)
        else:
            S.add(query_num)
        for i in range(1, N + 1):
            if i in S:
                A[i - 1] += len(S)
    print(*A)
    sys.exit()


if __name__ == "__main__":
    main()

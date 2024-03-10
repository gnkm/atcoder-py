"""E - Insert or Erase
https://atcoder.jp/contests/abc344/tasks/abc344_e

https://atcoder.jp/contests/abc344/editorial/9487
https://atcoder.jp/contests/abc344/submissions/50938793

tags: ['linked list']

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesls = lambda: list(input())  # input multi element single line str
i_memls = lambda n: [i_mesls() for _ in range(n)]  # input multi element multi line str


def main():
    N = i_sesli()
    seq_A_org = i_mesls()
    seq_A = [0] + seq_A_org + [-1]
    Q = i_sesli()
    queries = i_memls(Q)
    mae = {}
    ushiro = {}
    for i, a in enumerate(seq_A):
        if i < len(seq_A) - 1:
            mae[seq_A[i + 1]] = a
            ushiro[a] = seq_A[i + 1]

    for query in queries:
        if query[0] == "1":
            x = query[1]
            y = query[2]
            separated_node = ushiro[x]
            mae[y] = x
            mae[separated_node] = y
            ushiro[x] = y
            ushiro[y] = separated_node
        elif query[0] == "2":
            x = query[1]
            mae_x = mae[x]
            ushiro_x = ushiro[x]
            mae[ushiro_x] = mae_x
            ushiro[mae_x] = ushiro_x
            del mae[x]
            del ushiro[x]

    ans = []
    node = ushiro[0]
    while node != -1:
        ans.append(node)
        node = ushiro[node]

    print(*ans)
    sys.exit()


if __name__ == "__main__":
    main()

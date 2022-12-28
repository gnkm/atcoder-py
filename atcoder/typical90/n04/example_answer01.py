"""
https://atcoder.jp/contests/typical90/submissions/21907112
"""

H, W = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(H)]
L_trans = list(zip(*L))

col_sum = [sum(L[h]) for h in range(H)]
row_sum = [sum(L_trans[w]) for w in range(W)]
[print(*[col_sum[h] + row_sum[w] - L[h][w] for w in range(W)]) for h in range(H)]

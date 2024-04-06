"""A - Penalty Kick
https://atcoder.jp/contests/abc348/tasks/abc348_a

Result: AC
"""

N = int(input())
ans = ""
for i in range(N):
    if i % 3 == 2:
        ans += "x"
    else:
        ans += "o"
print(ans)

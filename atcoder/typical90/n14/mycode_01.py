"""014 - We Used to Sing a Song Together（★3）

https://atcoder.jp/contests/typical90/tasks/typical90_n

AGC 街道には N 人の小学生が住んでおり、小学生 i (1≤i≤N) の家は位置 A_i にあります。
また、小学校は N 校建てられており、小学校 j (1≤j≤N) は位置 B_j にあります。
AGC 街道に住む小学生は性格が悪く、どの人同士も険悪な関係になっているため、全員が別の学校に通うようにしたいです。

また、不便さは次のように定義されます。

- 小学生 i にとっての家から学校までの距離を E_i とするとき、不便さは距離の総和、すなわち E_1 + E_2 + ... + E_N である。
- ただし、位置 u から位置 v までの距離は ∣u−v∣

どの生徒も別の学校に通うという条件下における、不便さとして考えられる最小値を求めてください。
"""

# for debugging
import pkg_resources

if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic
else:
    debug = print

import pprint

# Scripts starts here.
import sys


mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int
i_mesli = lambda: mapl(int, input())               # input multi element single line int


def main():
    N = i_sesli()
    students = i_mesli()
    schools = i_mesli()
    students.sort()
    schools.sort()
    print(sum([abs(x - y) for x, y in zip(students, schools)]))
    sys.exit()


if __name__ == '__main__':
    main()

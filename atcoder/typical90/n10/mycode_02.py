"""010 - Score Sum Queries（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_j

Result: AC
"""

import sys
from itertools import accumulate

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: mapl(int, input())
i_memli = lambda n: [i_mesli() for _ in range(n)]


def main():
    N = i_sesli()
    student_points = i_memli(N)
    Q = i_sesli()
    queries = i_memli(Q)
    # class_points[i][j]: クラス i の学籍番号 j までの累積和
    class_points = [[0] * (N + 1) for _ in range(2)]
    for student_id, point_info in enumerate(student_points):
        class_num_index = point_info[0] - 1
        point = point_info[1]
        student_index = student_id + 1
        class_points[class_num_index][student_index] = point

    accumulate_points = [list(accumulate(l)) for l in class_points]
    for query in queries:
        student_index_left = query[0]
        student_index_right = query[1]
        ans_left = (
            accumulate_points[0][student_index_right]
            - accumulate_points[0][student_index_left - 1]
        )
        ans_right = (
            accumulate_points[1][student_index_right]
            - accumulate_points[1][student_index_left - 1]
        )
        print(f"{ans_left} {ans_right}")
    sys.exit()


if __name__ == "__main__":
    main()

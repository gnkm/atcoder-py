"""C - Ideal Holidays
https://atcoder.jp/contests/abc347/tasks/abc347_c

- 連続する予定が入らない日数が、平日の日数より小さいか着目する(こちらの方が見通しがよい？)
- 2 週間を考える(週をまたぐケースを含めるため)

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    N, holiday_num, weekday_num = map(int, input().split())
    schedules = mapl(int, input().split())
    days_per_week = holiday_num + weekday_num
    schedules_mod_1 = [i % days_per_week for i in schedules]
    schedules_mod_2 = [i % days_per_week + days_per_week for i in schedules]
    schedules_mod = schedules_mod_1 + schedules_mod_2
    schedules_mod.sort()
    # print(f"{schedules_mod = }")
    for i in range(len(schedules_mod) - 1):
        if schedules_mod[i + 1] - schedules_mod[i] >= weekday_num + 1:
            # print(f"{i = }")
            # print(f"{weekday_num = }")
            # print(f"{schedules_mod[i] = }")
            # print(f"{schedules_mod[i + 1] = }")
            print("Yes")
            sys.exit()
    print("No")
    sys.exit()


if __name__ == "__main__":
    main()

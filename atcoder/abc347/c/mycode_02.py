"""C - Ideal Holidays
https://atcoder.jp/contests/abc347/tasks/abc347_c

Result: WA
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    N, holiday_num, weekday_num = map(int, input().split())
    schedules = mapl(int, input().split())
    days_per_week = holiday_num + weekday_num
    schedules_nth_of_week = []
    for s in schedules:
        added = s % days_per_week
        if added == 0:
            added = days_per_week
        schedules_nth_of_week.append(added)
    if max(schedules_nth_of_week) - min(schedules_nth_of_week) < holiday_num:
        print("Yes")
    else:
        print("No")
    sys.exit()


if __name__ == "__main__":
    main()

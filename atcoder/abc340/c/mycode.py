"""C - Divide and Divide
https://atcoder.jp/contests/abc340/tasks/abc340_c
"""

# for debugging
import pkg_resources

if any([str(i).startswith("icecream") for i in pkg_resources.working_set]):
    import icecream

    debug = icecream.ic
else:
    debug = print

# Scripts starts here.
import math
import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int


def main():
    N = i_sesli()
    numbers = [N]
    cost = 0
    while True:
        if max(numbers) < 2:
            print(cost)
            break
        else:
            target_num = numbers[0]
            cost += target_num
            numbers.pop(0)
            numbers.append(math.floor(target_num / 2))
            numbers.append(math.ceil(target_num / 2))
            try:
                numbers.remove(1)
            except:
                continue

    sys.exit()


if __name__ == "__main__":
    main()

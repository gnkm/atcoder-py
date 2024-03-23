"""Title

URL

Problem statement here.
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


keyboard_unit = "wbwbwwbwbwbw"


def main():
    W, B = i_mesli()
    unit_num = (W + B) // len(keyboard_unit) + 2
    keyboard = unit_num * keyboard_unit
    is_exists = False
    for i, key in enumerate(keyboard):
        substr = keyboard[i : i + W + B]
        if substr.count("w") == W and substr.count("b") == B:
            is_exists = True
            break

    if is_exists:
        print("Yes")
    else:
        print("No")
    sys.exit()


if __name__ == "__main__":
    main()

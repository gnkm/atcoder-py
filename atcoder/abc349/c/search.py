import re
import sys


def main():
    S = input().upper() + "X"
    T = input()
    print(f"{S = }, {T = }")
    print(f"{re.search('.*'.join(T), S) = }")
    sys.exit()


if __name__ == "__main__":
    main()

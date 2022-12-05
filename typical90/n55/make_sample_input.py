"""Make sample input file for N55.

The example input on the official page(https://atcoder.jp/contests/typical90/tasks/typical90_bc)
is small size, you can use this script to create a large size example input.

Synopsis:
    python typical90/n55/make_sample_input.py input_file_name N P Q digit_of_A_i
Example:
    python typical90/n55/make_sample_input.py typical90/n55/input_11.txt 10 2 0 2
    python typical90/n55/make_sample_input.py typical90/n55/input_12.txt 100 97 1 8
"""

import icecream
debug = icecream.ic

from random import randrange
import sys


def main():
    output_file_name = sys.argv[1]
    size = int(sys.argv[2])
    assert 5 <= size <= 100
    p = int(sys.argv[3])
    assert 0 <= p <= 10 ** 9
    q = int(sys.argv[4])
    assert 0 <= q <= p
    digit_of_A_i = int(sys.argv[5])
    assert 0 <= digit_of_A_i <= 9
    sequence_A = [randrange(0, 0.1 * 10 ** digit_of_A_i) for _ in range(size)]

    with open(output_file_name, 'w', encoding='utf-8') as f:
        f.write(f'{size} {p} {q}')
        f.write('\n')
        f.write(' '.join(map(str, sequence_A)))

    sys.exit()


if __name__ == '__main__':
    main()

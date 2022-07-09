import icecream, pprint  # for debugging
from math import sin, cos, radians, sqrt
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, input()))          # input multi element single line int

sys.setrecursionlimit(1000000)

def main():
    a, b, d = i_mesli()
    if a == 0 and b == 0:
        print('0 0')
        sys.exit()

    r = sqrt(a ** 2 + b ** 2)
    cos_theta_0 = a / r
    sin_theta_0 = b / r
    theta_d = radians(d)
    new_a = r * (cos_theta_0 * cos(theta_d) - sin_theta_0 * sin(theta_d))
    new_b = r * (sin_theta_0 * cos(theta_d) + cos_theta_0 * sin(theta_d))
    print(f'{new_a} {new_b}')

if __name__ == '__main__':
    main()

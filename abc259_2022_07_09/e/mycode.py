import icecream, pprint  # for debugging
import math
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int
i_seslf = lambda: float(input()[0])                # input single element single line float
i_sesls = lambda: str(input()[0])                  # input single element single line str
i_semli = lambda n: [i_slsei() for _ in range(n)]  # input single element multi line int
i_semlf = lambda n: [i_slsef() for _ in range(n)]  # input single element multi line float
i_semls = lambda n: [i_slses() for _ in range(n)]  # input single element multi line str
i_mesli = lambda: list(map(int, input()))          # input multi element single line int
i_meslf = lambda: list(map(float, input()))        # input multi element single line float
i_mesls = lambda: list(input())                    # input multi element single line str
i_memli = lambda n: [i_mesli() for _ in range(n)]    # input multi element multi line int
i_memlf = lambda n: [i_meslf() for _ in range(n)]    # input multi element multi line float
i_memls = lambda n: [i_mesls() for _ in range(n)]    # input multi element multi line str

sys.setrecursionlimit(1000000)

def main():
    N = i_sesli()
    a_elements = []
    for _ in range(N):
        m_i = i_sesli()
        _a_i_elements = i_memli(m_i)
        a_elements.append(_a_i_elements)

    a_list = []
    for a_i_elements in a_elements:
        a_i = 1
        for items in a_i_elements:
            a_i *= items[0] ** items[1]
        a_list.append(a_i)

    lcm_list = []
    for i, _ in enumerate(a_list):
        new_a_list = a_list
        new_a_list[i] = 1

if __name__ == '__main__':
    main()

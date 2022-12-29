"""002 - Encyclopedia of Parentheses（★3）

https://atcoder.jp/contests/typical90/tasks/typical90_b

長さ N の正しいカッコ列をすべて、辞書順に出力してください。

ただし、正しいカッコ列は次のように定義されています :

- `()` は正しいカッコ列である
- S が正しいカッコ列であるとき、文字列 `(` + S + `)` は正しいカッコ列である
- S,T が正しいカッコ列であるとき、文字列 S + T は正しいカッコ列である
- それ以外の文字列はすべて、正しいカッコ列でない

例えば、

- `()()`
- `(()())(())`
- `()()()()()()()()`

は正しいカッコ列ですが、

- `)(`
- `)))()(((`
- `((((a))))`

は正しいカッコ列ではありません。

また、 `(` の方が `)` よりも辞書順で早いものとします。

Result: WA
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

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')


input = lambda: sys.stdin.readline().rstrip('\r\n').split()


sys.setrecursionlimit(1000000)


def main():
    length = int(input()[0])
    [print(p) for p in sorted(parentheses_wa(length))]
    sys.exit()


def parentheses(length):
    return []


def parentheses_wa(length):
    """Wrong answer.

    Some answers are not contained.
    e.g.
    length = 8
    `(())(())`

    length = 10
    `((())(()))`
    """
    if length % 2 != 0:
        return [""]

    if length == 2:
        return ["()"]

    smaller_parentheses = parentheses_wa(length - 2)
    return list(set(
        [f"(){p}" for p in smaller_parentheses] \
            + [f"({p})" for p in smaller_parentheses] \
            + [f"{p}()" for p in smaller_parentheses]
    ))


if __name__ == '__main__':
    main()

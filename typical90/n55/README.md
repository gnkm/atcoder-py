# 055 - Select 5（★2）

## 問題

N 個の整数 A_1, A_2, ⋯, A_N があります。 この中から 5 個を選ぶ方法のうち、これら 5 個の整数の積を P で割ると Q 余るようなものが何通りあるか求めてください。

### 制約

実行時間制限: 5 sec / メモリ制限: 1024 MB
制約
- 5 <= N <= 100
- 0 <= A_i <= 10 ** 9
- 0 <= Q <= P <= 10 ** 9

URL: https://atcoder.jp/contests/typical90/tasks/typical90_bc

## 回答

### `mycode_01_tle.py`: TLE(5515 ms)

`itertools.combinations()`, `functools.reduce()` を使用。

### `example_answer_01.py`: TLE(5515 ms)

5 重の `for` で実装。

### `example_answer_02.py`: AC(3101 ms)

`itertools.combinations()` とリスト内包表記でワンライナーにしたコード。

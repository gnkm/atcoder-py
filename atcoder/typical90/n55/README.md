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

## 回答コード

### `mycode_01_tle.py`: TLE(5515 ms)

`itertools.combinations()`, `functools.reduce()` を使用。

### `example_answer_01.py`: TLE(5515 ms)

5 重の `for` で実装。

### `example_answer_01_2.py`

`example_answer_01.py` をより短くしたもの。

### `example_answer_02.py`: AC(3101 ms)

`itertools.combinations()` とリスト内包表記でワンライナーにしたコード。

## 速度比較

### 環境

```
python -V
# =>
# Python 3.7.10 (51efa818fd9b, Apr 04 2021, 12:03:51)
# [PyPy 7.3.4 with GCC Apple LLVM 12.0.0 (clang-1200.0.32.29)]
```

```
uname -a
# => Darwin s-mba.local 21.6.0 Darwin Kernel Version 21.6.0: Mon Aug 22 20:20:05 PDT 2022; root:xnu-8020.140.49~2/RELEASE_ARM64_T8101 arm64 arm Darwin
```

```
sw_vers
# =>
# ProductName:	macOS
# ProductVersion:	12.6
# BuildVersion:	21G115
```

```
pyenv --version
# => pyenv 2.3.1-17-g9f2cba3d
```

```
hyperfine --version
# => hyperfine 1.15.0
```

### 比較

#### `mycode_01_tle.py`

```
hyperfine -r 1000 --ignore-failure python typical90/n55/mycode_01_tle.py < typical90/n55/input_13.txt
```

output

```
  Time (mean ± σ):      33.2 ms ±   3.3 ms    [User: 21.5 ms, System: 8.1 ms]
  Range (min … max):    31.9 ms … 114.7 ms    1000 runs
```

#### `example_answer_01.py`

```
hyperfine -r 1000 --ignore-failure python typical90/n55/example_answer_01.py < typical90/n55/input_13.txt
```

output

```
  Time (mean ± σ):      33.2 ms ±   2.6 ms    [User: 21.5 ms, System: 8.1 ms]
  Range (min … max):    31.5 ms …  90.1 ms    1000 runs
```

#### `example_answer_01_2.py`

```
hyperfine -r 1000 --ignore-failure python typical90/n55/example_answer_01_2.py < typical90/n55/input_13.txt
```

Output

```
  Time (mean ± σ):      32.8 ms ±   0.5 ms    [User: 21.4 ms, System: 8.0 ms]
  Range (min … max):    32.0 ms …  37.8 ms    1000 runs
```

#### `example_answer_02.py`

```
hyperfine -r 1000 --ignore-failure python typical90/n55/example_answer_02.py < typical90/n55/input_13.txt
```

Output

```
  Time (mean ± σ):      32.7 ms ±   0.6 ms    [User: 21.4 ms, System: 8.0 ms]
  Range (min … max):    31.6 ms …  39.3 ms    1000 runs
```

### まとめ

| コード                   | mean | σ   | min  | max   |
|:------------------------:|-----:|----:|-----:|------:|
| `mycode_01_tle.py`       | 33.2 | 3.3 | 31.9 | 114.7 |
| `example_answer_01.py`   | 33.2 | 2.6 | 31.5 |  90.1 |
| `example_answer_01_2.py` | 32.8 | 0.5 | 32.0 |  37.8 |
| `example_answer_02.py`   | 32.7 | 0.6 | 31.6 |  39.3 |

## 差異が生じる原因

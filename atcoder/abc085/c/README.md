# ABC085C - Otoshidama

## 問題文

### オリジナル

日本でよく使われる紙幣は、10000 円札、5000 円札、1000 円札です。以下、「お札」とはこれらのみを指します。

青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N 枚入っていて、合計で Y 円だったそうですが、嘘かもしれません。このような状況がありうるか判定し、ありうる場合はお年玉袋の中身の候補を一つ見つけてください。なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。

### 書き換え

下記を満たす非負整数 $(x, y, z)$ の組を求めよ。

$$
\begin{equation*}
  \left\{ 
  \begin{alignedat}{3}
       & x +{}   & y +{} & z &= N \\
    10 & x +{} 5 & y +{} & z &= Y
  \end{alignedat} 
  \right.
\end{equation*}
$$

## 解法

### `mycode_01.py`

$x$ を $0 \le x \le N$ の範囲で探すが、$y$ は $0 \le y \le N - x$ の範囲で探す。

### `mycode_02.py`

与えられた条件は下記と同じ。

$$
\begin{equation*}
  \left\{ 
  \begin{alignedat}{2}
      & x +{} & y &= N - z\\
    2 & x +{} & y &= \frac{Y - z}{5}
  \end{alignedat} 
  \right.
\end{equation*}
$$

これらを満たす非負整数の組 $(x, y)$ が存在するには下記が必要である。

- $0 \le z,$
- $z \le N,$
- $z \le Y.$

また $2 x + y$ は非負整数であるから下記が必要である。

- $z \equiv Y(\text{mod} 5).$

さらに $x + y \le 2 x + y \le 2(x + y)$ であるから

$$
N - z \le \frac{Y - z}{5} \le 2 (N - z),
$$

すなわち

- $\frac{5 N - Y}{4} \le z$
- $z \le \frac{10 N - Y}{9}$

も必要である。
$z$ が満たすべき条件をまとめると下記のとおり。

- $0 \le z,$
- $\frac{5 N - Y}{4} \le z$
- $z \le \frac{10 N - Y}{9}$

この条件を満たす非負整数 $z$ を求め、その後$x, y$ を求める。

### `mycode_03.py`

$$
\begin{equation*}
  \left\{ 
  \begin{alignedat}{3}
       & x +{}   & y +{} & z &= N \\
    10 & x +{} 5 & y +{} & z &= Y
  \end{alignedat} 
  \right.
\end{equation*}
$$

から $z$ を削除すると

$$
y = \frac{Y - N - 9x}{4}
$$

となる。これを満たす非負整数を探す。

$x$ の範囲は $y \ge 0$ より

$$
0 \le x \le \frac{Y - N}{9}
$$

である。

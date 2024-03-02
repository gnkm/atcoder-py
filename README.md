# AtCoder(PyPy)

## Problems

- [AtCoder](https://atcoder.jp/home)
- [AtCoder Beginners Selection](https://atcoder.jp/contests/abs/tasks)
- [競プロ典型 90 問](https://atcoder.jp/contests/typical90)
- [AtCoder Problems](https://kenkoooo.com/atcoder/#/table/)

## Usage

### Create virtual env

```
asdf install python pypy3.10-7.3.12
poetry env use $HOME/.asdf/installs/python/pypy3.10-7.3.12/bin/python
```

### Prepare

```
poetry shell
poetry install
```

### Execute

```
python xxx.py < input.txt
```

### Exit virtual env

```
exit
```

### Create Contest Directory

```
mkdir -p atcoder/abcXXX
python -c 'import string; [print(s) for s in list(string.ascii_lowercase)[:6]]' | xargs -I@ mkdir -p atcoder/abcXXX/@
python -c 'import string; [print(s) for s in list(string.ascii_lowercase)[:6]]' | xargs -I@ cp template.py atcoder/abcXXX/@/mycode.py
python -c 'import string; [print(s) for s in list(string.ascii_lowercase)[:6]]' | xargs -I@ touch atcoder/abcXXX/@/input_0{1,2}.txt
```

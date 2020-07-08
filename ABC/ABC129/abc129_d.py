# 問題URL: https://atcoder.jp/contests/abc129/tasks/abc129_d
# 解答URL: https://atcoder.jp/contests/abc129/submissions/15078490

import sys
import numpy as np


def read():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, read().split())
    s = np.array([[i == "." for i in read()] for _ in range(h)], dtype=int)
    left = s.copy()
    right = s.copy()
    up = s.copy()
    down = s.copy()
    for i in range(w - 1):
        left[:, i + 1] = (left[:, i] + 1) * s[:, i + 1]
        right[:, -i - 2] = (right[:, -i - 1] + 1) * s[:, -i - 2]
    for i in range(h - 1):
        up[i + 1] = (up[i] + 1) * s[i + 1]
        down[-i - 2] = (down[-i - 1] + 1) * s[-i - 2]
    print((left + right + up + down).max() - 3)


if __name__ == '__main__':
    main()

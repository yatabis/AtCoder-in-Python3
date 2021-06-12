# 問題URL: https://atcoder.jp/contests/abc132/tasks/abc132_f
# 解答URL: https://atcoder.jp/contests/abc132/submissions/23362970

from math import ceil, sqrt
import numpy as np


def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    m = set()
    for i in range(1, ceil(sqrt(n)) + 1):
        m.add(i)
        m.add(n // i + 1)
    dm = np.diff(np.array(sorted(list(m))))
    dp = np.ones(len(m) - 1, dtype=np.int64)
    for _ in range(k):
        cum = np.cumsum(dp * dm % mod) % mod
        dp = cum[::-1]
    print(dp[0])


if __name__ == '__main__':
    main()

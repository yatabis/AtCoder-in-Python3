# 問題URL: https://atcoder.jp/contests/abc126/tasks/abc126_c
# 解答URL: https://atcoder.jp/contests/abc126/submissions/14634593

from math import ceil, log2

n, k = map(int, input().split())
print(sum(0.5 ** max(ceil(log2(k / i)), 0) for i in range(1, n + 1)) / n)

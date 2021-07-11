# 問題URL: https://atcoder.jp/contests/abc134/tasks/abc134_b
# 解答URL: https://atcoder.jp/contests/abc134/submissions/24157832

from math import ceil

n, d = map(int, input().split())
print(ceil(n / (2 * d + 1)))

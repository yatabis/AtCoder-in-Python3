# 問題URL: https://atcoder.jp/contests/abc131/tasks/abc131_c
# 解答URL: https://atcoder.jp/contests/abc131/submissions/23183772

from math import gcd

a, b, c, d = map(int, input().split())
cd = c * d // gcd(c, d)
fc = b // c - (a - 1) // c
fd = b // d - (a - 1) // d
fcd = b // cd - (a - 1) // cd
print(b - (a - 1) - fc - fd + fcd)

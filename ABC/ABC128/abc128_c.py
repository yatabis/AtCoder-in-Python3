# 問題URL: https://atcoder.jp/contests/abc128/tasks/abc128_c
# 解答URL: https://atcoder.jp/contests/abc128/submissions/14706552

from itertools import product

n, m = map(int, input().split())
l = [[int(i) for i in input().split()] for _ in range(m)]
p = [int(i) for i in input().split()]
c = 0
for sw in product((0, 1), repeat=n):
    for i in range(m):
        if sum(sw[si - 1] for si in l[i][1:]) % 2 != p[i]:
            break
    else:
        c += 1
print(c)

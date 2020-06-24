# 問題URL: https://atcoder.jp/contests/abc127/tasks/abc127_c
# 解答URL: https://atcoder.jp/contests/abc127/submissions/14655419

n, m = map(int, input().split())
lmax, rmin = 0, n
for _ in range(m):
    l, r = map(int, input().split())
    lmax = max(l, lmax)
    rmin = min(r, rmin)
print(max(rmin - lmax + 1, 0))

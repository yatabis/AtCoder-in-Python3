# 問題URL: https://atcoder.jp/contests/abc130/tasks/abc130_d
# 解答URL: https://atcoder.jp/contests/abc130/submissions/16222018

n, k = map(int, input().split())
a = [int(i) for i in input().split()]
i = 0
s = 0
ans = 0
for j in range(n):
    s += a[j]
    while s >= k:
        s -= a[i]
        i += 1
    ans += i
print(ans)

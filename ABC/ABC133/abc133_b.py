# 問題URL: https://atcoder.jp/contests/abc133/tasks/abc133_b
# 解答URL: https://atcoder.jp/contests/abc133/submissions/23637165

n, d = map(int, input().split())
x = [[int(i) for i in input().split()] for _ in range(n)]
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        dist = sum((x[i][k] - x[j][k])**2 for k in range(d))**0.5
        ans += int(dist) == dist
print(ans)

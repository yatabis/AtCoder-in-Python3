# 問題URL: https://atcoder.jp/contests/abc133/tasks/abc133_d
# 解答URL: https://atcoder.jp/contests/abc133/submissions/23637887

n = int(input())
a = [int(i) for i in input().split()]
x = [0] * n
x[0] = sum(a[i] * (1 - i % 2 * 2) for i in range(n))
for i in range(n - 1):
    x[i + 1] = 2 * a[i] - x[i]
print(*x)

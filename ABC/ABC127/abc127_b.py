# 問題URL: https://atcoder.jp/contests/abc127/tasks/abc127_b
# 解答URL: https://atcoder.jp/contests/abc127/submissions/14655294

r, d, x = map(int, input().split())
for _ in range(10):
    x = r * x - d
    print(x)

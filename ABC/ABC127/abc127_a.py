# 問題URL: https://atcoder.jp/contests/abc127/tasks/abc127_a
# 解答URL: https://atcoder.jp/contests/abc127/submissions/14655259

a, b = map(int, input().split())
if a <= 5:
    print(0)
elif a <= 12:
    print(b // 2)
else:
    print(b)

# 問題URL: https://atcoder.jp/contests/abc130/tasks/abc130_c
# 解答URL: https://atcoder.jp/contests/abc130/submissions/16221649

w, h, x, y = map(int, input().split())
print(w * h / 2, int(2 * x == w and 2 * y == h))

# 問題URL: https://atcoder.jp/contests/abc129/tasks/abc129_a
# 解答URL: https://atcoder.jp/contests/abc129/submissions/15076801

p, q, r = map(int, input().split())
print(p + q + r - max(p, q, r))

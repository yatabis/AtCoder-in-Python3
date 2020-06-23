# 問題URL: https://atcoder.jp/contests/abc126/tasks/abc126_a
# 解答URL: https://atcoder.jp/contests/abc126/submissions/14634149

_, k = [int(i) - 1 for i in input().split()]
s = input()
print(s[:k] + s[k].lower() + s[k + 1:])

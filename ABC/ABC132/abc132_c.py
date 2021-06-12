# 問題URL: https://atcoder.jp/contests/abc132/tasks/abc132_c
# 解答URL: https://atcoder.jp/contests/abc132/submissions/23357358

n = int(input())
d = sorted(map(int, input().split()))
left, right = d[n // 2 - 1], d[n // 2]
print(right - left)

# 問題URL: https://atcoder.jp/contests/abc134/tasks/abc134_e
# 解答URL: https://atcoder.jp/contests/abc134/submissions/24159068

from bisect import bisect

n = int(input())
colors = [-int(input())]
for _ in range(n - 1):
    a = -int(input())
    if a >= colors[-1]:
        colors.append(a)
    else:
        i = bisect(colors, a)
        colors[i] = a
print(len(colors))

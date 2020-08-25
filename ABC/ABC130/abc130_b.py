# 問題URL: https://atcoder.jp/contests/abc130/tasks/abc130_b
# 解答URL: https://atcoder.jp/contests/abc130/submissions/16221202

n, x = map(int, input().split())
l = [int(i) for i in input().split()]
p = 0
for i in range(n):
    p += l[i]
    if p > x:
        print(i + 1)
        break
else:
    print(n + 1)

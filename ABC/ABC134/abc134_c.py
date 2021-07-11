# 問題URL: https://atcoder.jp/contests/abc134/tasks/abc134_c
# 解答URL: https://atcoder.jp/contests/abc134/submissions/24157973

n = int(input())
a = [int(input()) for _ in range(n)]
first = max(a)
if a.count(first) > 1:
    print(*[first] * n, sep="\n")
else:
    second = max(ai for ai in a if ai < first)
    print(*[first if ai < first else second for ai in a], sep="\n")

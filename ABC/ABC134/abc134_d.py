# 問題URL: https://atcoder.jp/contests/abc134/tasks/abc134_d
# 解答URL: https://atcoder.jp/contests/abc134/submissions/24158327

n = int(input())
a = [int(i) for i in input().split()]
b = [0] * n
for i in range(n, 0, -1):
    b[i - 1] = (sum(b[i - 1::i]) % 2) ^ a[i - 1]
print(sum(b))
print(*[i + 1 for i, bi in enumerate(b) if bi])

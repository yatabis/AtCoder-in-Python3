# 問題URL: https://atcoder.jp/contests/abc132/tasks/abc132_b
# 解答URL: https://atcoder.jp/contests/abc132/submissions/23357098

n = int(input())
p = [int(i) for i in input().split()]
ans = 0
for i in range(n - 2):
    ans += sorted(p[i:i + 3])[1] == p[i + 1]
print(ans)

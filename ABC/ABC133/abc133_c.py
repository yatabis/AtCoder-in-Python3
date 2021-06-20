# 問題URL: https://atcoder.jp/contests/abc133/tasks/abc133_c
# 解答URL: https://atcoder.jp/contests/abc133/submissions/23637300

l, r = map(int, input().split())
if r - l > 673:
    print(0)
else:
    ans = 2019
    for i in range(l, r):
        for j in range(l + 1, r + 1):
            ans = min(i * j % 2019, ans)
    print(ans)

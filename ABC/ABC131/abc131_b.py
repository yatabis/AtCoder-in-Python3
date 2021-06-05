# 問題URL: https://atcoder.jp/contests/abc131/tasks/abc131_b
# 解答URL: https://atcoder.jp/contests/abc131/submissions/23183637

n, l = map(int, input().split())
apples = [l + i for i in range(n)]
print(sum(apples) - min(apples, key=abs))

# 問題URL: https://atcoder.jp/contests/abc132/tasks/abc132_a
# 解答URL: https://atcoder.jp/contests/abc132/submissions/23356286

from collections import Counter

s = input()
print("Yes" if tuple(Counter(s).values()) == (2, 2) else "No")

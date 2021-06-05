# 問題URL: https://atcoder.jp/contests/abc131/tasks/abc131_a
# 解答URL: https://atcoder.jp/contests/abc131/submissions/23183331

s = input()
if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
    print("Bad")
else:
    print("Good")

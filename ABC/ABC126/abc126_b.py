# 問題URL: https://atcoder.jp/contests/abc126/tasks/abc126_b
# 解答URL: https://atcoder.jp/contests/abc126/submissions/14634329

s = input()
a = 1 <= int(s[:2]) <= 12
b = 1 <= int(s[2:]) <= 12
if a and b:
    print("AMBIGUOUS")
elif a:
    print("MMYY")
elif b:
    print("YYMM")
else:
    print("NA")

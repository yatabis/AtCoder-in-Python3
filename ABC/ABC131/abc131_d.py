# 問題URL: https://atcoder.jp/contests/abc131/tasks/abc131_d
# 解答URL: https://atcoder.jp/contests/abc131/submissions/23183885

import sys
from operator import itemgetter


def read():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    job = sorted([[int(i) for i in read().split()] for _ in range(n)], key=itemgetter(1))
    t = 0
    for a, b in job:
        t += a
        if t > b:
            print("No")
            break
    else:
        print("Yes")


if __name__ == '__main__':
    main()

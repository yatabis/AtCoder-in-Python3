# 問題URL: https://atcoder.jp/contests/abc132/tasks/abc132_e
# 解答URL: https://atcoder.jp/contests/abc132/submissions/23359973

from collections import deque
import sys


def read():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, read().split())
    al = [[] for _ in range(n)]
    for _ in range(m):
        u, v = [int(i) - 1 for i in read().split()]
        al[u].append(v)
    s, t = [int(i) - 1 for i in read().split()]
    todo = deque([(s, 0)])
    seen = set()
    while todo:
        u, d = todo.popleft()
        if (u, d % 3) in seen:
            continue
        seen.add((u, d % 3))
        if u == t and d % 3 == 0:
            print(d // 3)
            break
        for v in al[u]:
            todo.append((v, d + 1))
    else:
        print(-1)


if __name__ == '__main__':
    main()

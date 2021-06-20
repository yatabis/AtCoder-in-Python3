# 問題URL: https://atcoder.jp/contests/abc133/tasks/abc133_e
# 解答URL: https://atcoder.jp/contests/abc133/submissions/23644622

import sys


def read():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, read().split())
    al = [[] for _ in range(n)]
    mod = 10**9 + 7
    for _ in range(n - 1):
        a, b = [int(i) - 1 for i in read().split()]
        al[a].append(b)
        al[b].append(a)
    c = [0] * n
    m = [0] * n
    c[0] = k
    m[0] = k - 1
    todo = [(u, 0) for u in al[0]]
    seen = {0}
    while todo:
        v, p = todo.pop()
        if v in seen:
            continue
        seen.add(v)
        c[v] = m[p]
        m[v] = max(m[p] - 1, k - 2)
        m[p] -= 1
        for u in al[v]:
            todo.append((u, v))
    ans = 1
    for ci in c:
        ans = ans * ci % mod
    print(ans)


if __name__ == '__main__':
    main()

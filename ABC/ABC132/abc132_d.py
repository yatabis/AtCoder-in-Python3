# 問題URL: https://atcoder.jp/contests/abc132/tasks/abc132_d
# 解答URL: https://atcoder.jp/contests/abc132/submissions/23359744


from functools import lru_cache


@lru_cache(maxsize=2048, typed=True)
def fact(n, mod):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return n * fact(n - 1, mod) % mod


@lru_cache(maxsize=2048, typed=True)
def inv(n, mod):
    return pow(fact(n, mod), mod - 2, mod)


@lru_cache(maxsize=2048, typed=True)
def ncr(n, r, mod):
    r = min(n - r, r)
    if r < 0:
        return 0
    if r == 0:
        return 1
    over = fact(n, mod) * inv(n - r, mod) % mod
    under = inv(r, mod)
    return over * under % mod


def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    for i in range(n + 1):
        fact(i, mod)
    for i in range(1, k + 1):
        print(ncr(k - 1, i - 1, mod) * ncr(n - k + 1, i, mod) % mod)


if __name__ == '__main__':
    main()

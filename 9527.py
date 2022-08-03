import sys
input = sys.stdin.readline

x, y = map(int, input().split())


def calc(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    neareast2n = n
    exp = -1
    while neareast2n:
        neareast2n >>= 1
        exp += 1
    neareast2n = 1 << exp
    count = exp * 2 ** (exp - 1) + 1
    count += n - neareast2n
    count += calc(n - neareast2n)
    return count

print(calc(y) - calc(x-1))

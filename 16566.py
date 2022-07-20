import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m, k = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()

seq = list(map(int, input().split()))
arr = [i for i in range(4000001)]


def union(a, b):
    a = find(a)
    b = find(b)
    arr[a] = b


def find(a):
    if arr[a] == a:
        return a
    arr[a] = find(arr[a])
    return arr[a]


def binary_search(ch):
    low = 0
    high = len(cards)
    while low < high:
        mid = (high + low) // 2
        val = cards[find(mid)]
        if val <= ch:
            low = mid + 1
            continue
        if val > ch:
            high = mid
            continue
    print(str(cards[find(high)]) + "\n")
    if high < len(cards) - 1:
        union(find(high), find(high)+1)


for ch in seq:
    binary_search(ch)

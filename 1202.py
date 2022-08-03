import sys
from bisect import bisect_left
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jewels = []
bags = []


for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))
jewels.sort(key=lambda x: x[0])
for _ in range(k):
    c = int(input())
    bags.append(c)
bags.sort()

total = 0

heap = []
i = 0
j = 0
while i < k:
    while j < n and jewels[j][0] <= bags[i]:
        heapq.heappush(heap, -jewels[j][1])
        j += 1

    if heap:
        total -= heapq.heappop(heap)
    i += 1

print(total)

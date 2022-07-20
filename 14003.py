import sys
from bisect import bisect_left
input = sys.stdin.readline

a = int(input())
seq = list(map(int, input().split()))
index_history = []
sequence_list_val = [seq[0]]
for index, val in enumerate(seq):

    if sequence_list_val[-1] < val:
        sequence_list_val.append(val)
        index_history.append(len(sequence_list_val) - 1)
        continue
    if sequence_list_val[0] > val:
        sequence_list_val[0] = val
        index_history.append(0)
        continue

    r = bisect_left(sequence_list_val, val)
    sequence_list_val[r] = val
    index_history.append(r)

print(len(sequence_list_val))
i = len(sequence_list_val) - 1
history = []
for t,index in enumerate(reversed(index_history)):
    if i == index:
        history.append(seq[len(seq) - 1 - t])
        i -= 1

print(" ".join(map(str, reversed(history))))
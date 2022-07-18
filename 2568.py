import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
lines = []
a_lines = set()
for i in range(n):
    a,b = map(int, input().split())
    lines.append([a,b])
    a_lines.add(a)
lines.sort(key=lambda x:x[0])

lis = []
history = []

for line in lines:
    a = line[0]
    b = line[1]
    if not lis:
        lis.append(b)
        history.append(0)
        continue
    if lis[-1] < b:
        lis.append(b)
        history.append(len(lis) - 1)

    for lis_index in range(len(lis)):
        if lis[lis_index] > b:
            lis[lis_index] = b
            history.append(lis_index)
            break

real_lis = []
history.reverse()
cur_order = len(lis) - 1
for history_index, order in enumerate(history):
    if order == cur_order:
        real_lis.append(lines[len(lines) - 1-history_index][0])
        cur_order -= 1

for i in real_lis:
    a_lines.remove(i)
print(str(len(a_lines)) + "\n")
for i in a_lines:
    print(str(i) + "\n")
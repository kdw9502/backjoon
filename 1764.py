N, M = map(int, input().split())
names = []
both = []
for i in range(N):
    names.append(input())
for i in range(M):
    names.append(input())
names.sort()

for i in range(len(names) - 1):
    if names[i] == names[i+1]:
        both.append(names[i])

print(len(both))
print(*sorted(both), sep="\n")
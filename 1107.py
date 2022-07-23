channel = int(input())
val = int(input())
if val:
    broken = input().split()
else:
    broken = []

sol = abs(channel - 100)
for i in range(1000001):
    for ch in str(i):
        if ch in broken:
            break
    else:
        sol = min(sol, abs(channel-i) + len(str(i)))

print(sol)
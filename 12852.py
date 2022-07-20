n = int(input())

arr = [0 for i in range(n + 1)]
history = [0 for i in range(n + 1)]
arr[n] = 0
arr[n - 1] = 1
for i in range(n - 1, 0, -1):
    a = b = c = n
    if i * 3 <= n:
        a = arr[i * 3] + 1
    if i * 2 <= n:
        b = arr[i * 2] + 1
    c = arr[i + 1] + 1
    val = min(a, b, c)
    if val == a:
        history[i] = 0
    elif val == b:
        history[i] = 1
    elif val == c:
        history[i] = 2
    arr[i] = val

print(arr[1])
stack = [1]
index = 1
while index != n:
    if history[index] == 0:
        index = index * 3
    elif history[index] == 1:
        index = index * 2
    elif history[index] == 2:
        index = index + 1
    stack.append(index)
stack.reverse()
print(" ".join(map(str,stack)))

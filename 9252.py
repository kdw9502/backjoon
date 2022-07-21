str1 = input()
str2 = input()
right = 1
down = 2
diag = 3

array = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
history = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i, chr1 in enumerate(str1):
    for j, chr2 in enumerate(str2):
        if chr1 == chr2:
            array[i+1][j+1] = array[i][j] + 1
            history[i+1][j+1] = diag
        else:
            array[i + 1][j + 1] = max(array[i][j + 1], array[i + 1][j])
            if array[i][j+1] >= array[i+1][j]:
                history[i+1][j+1] = down
            else:
                history[i + 1][j + 1] = right


print(array[len(str1)][len(str2)])
i = len(str1)
j = len(str2)
string = []
while i and j:
    if history[i][j] == diag:
        i -= 1
        j -= 1
        string.append(str1[i])
    elif history[i][j] == right:
        j -= 1
    elif history[i][j] == down:
        i -= 1
print("".join(reversed(string)))
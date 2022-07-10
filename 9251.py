str1 = input()
str2 = input()
array = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i, chr1 in enumerate(str1):
    for j, chr2 in enumerate(str2):
        if chr1 == chr2:
            array[i+1][j+1] = array[i][j] + 1
        else:
            array[i + 1][j + 1] = max(array[i][j+1], array[i+1][j])

print(array[len(str1)][len(str2)])
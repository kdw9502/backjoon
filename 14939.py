import sys
input = sys.stdin.readline

arr = [[0 for i in range(10)] for _ in range(10)]

for i in range(10):
    string = input().rstrip()
    for j, ch in enumerate(string):
        if ch == "O":
            arr[i][j] = 1

def get_count(bit):
    count = 0
    temp_arr = [[arr[i][j] for j in range(10)] for i in range(10)]
    for i in range(10):
        if bit & (1 << i):
            temp_arr[0][i] ^= 1
            temp_arr[1][i] ^= 1
            if i > 0:
                temp_arr[0][i - 1] ^= 1
            if i < 9:
                temp_arr[0][i + 1] ^= 1
            count += 1
    for i in range(1,10):
        for j in range(10):
            if temp_arr[i-1][j] == 1:
                temp_arr[i][j] ^= 1
                temp_arr[i-1][j] ^= 1
                if i < 9:
                    temp_arr[i+1][j] ^= 1
                if j > 0:
                    temp_arr[i][j - 1] ^= 1
                if j < 9:
                    temp_arr[i][j + 1] ^= 1
                count += 1
    if any(temp_arr[9]):
        return 1025
    return count

min_count = 1025
for j in range(10):
    for bit in range(1024):
        count = get_count(bit)
        if count < min_count:
            min_count = count
if min_count == 1025:
    print(-1)
else:
    print(min_count)

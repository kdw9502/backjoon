n,m = input().split(" ")
n = int(n)
m = int(m)

def main():
    array = []
    for i in range(n):
        array.append(input().strip())

    min_val = 50*50
    for offset_x in range(n-7):
        for offset_y in range(m-7):
            val = get_count(array, offset_x, offset_y)
            if val < min_val:
                min_val = val

    print(min_val)


def get_count(array, x, y):
    count = 0
    for i in range(8):
        for j in range(8):
            letter = array[x+i][y+j]
            if (j + i) % 2 == 0 and letter == "W":
                count = count + 1
            if (j + i) % 2 == 1 and letter == "B":
                count = count + 1

    if count > 32:
        count = 64 - count
    return count

main()
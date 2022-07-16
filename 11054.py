length = int(input())
seq = list(map(int,input().split()))


def get_increasing_seq(seq, max):
    if not seq:
        return []
    result = []
    for val in seq:
        if val >= max:
            continue
        if not result:
            result.append(val)
        for i in range(len(result)):
            if result[i] > val:
                if i == 0:
                    result[i] = val
                elif val > result[i - 1]:
                    result[i] = val

            if result[i] < val:
                if len(result) == i + 1:
                    result.append(val)
                elif result[i + 1] > val:
                    result[i + 1] = val
    return result


max = 0
for i in range(length):
    inc = len(get_increasing_seq(seq[:i], seq[i]))
    dec = len(get_increasing_seq(list(reversed(seq[i+1:])) ,seq[i]))
    bi_len = inc + dec + 1
    if bi_len > max:
        max = bi_len
print(max)
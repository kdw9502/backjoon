input()
seq = list(map(int, input().split()))

sequence_list_val = [seq[0]]
for val in seq:
    for i in range(len(sequence_list_val)):
        if sequence_list_val[i] > val:
            if i == 0:
                sequence_list_val[i] = val
            elif val > sequence_list_val[i - 1]:
                sequence_list_val[i] = val

        if sequence_list_val[i] < val:
            if len(sequence_list_val) == i + 1:
                sequence_list_val.append(val)
            elif sequence_list_val[i + 1] > val:
                sequence_list_val[i + 1] = val

print(len(sequence_list_val))

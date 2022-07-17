from collections import defaultdict as dict
n, s = map(int, input().split())
seq = list(map(int, input().split()))

left = seq[:n // 2]
right = seq[n // 2:]

left_dict = dict(int)
right_dict = dict(int)
left_dict[0] = 1
right_dict[0] = 1

def check(seq, dictionary, sum):
    if not seq:
        return

    dictionary[sum + seq[0]] += 1

    check(seq[1:], dictionary, sum + seq[0])
    check(seq[1:], dictionary, sum)


check(left, left_dict, 0)
check(right, right_dict, 0)
count = 0
for i in left_dict:
    if (s - i) in right_dict:
        count += left_dict[i] * right_dict[s-i]
if s == 0:
    count -= 1
print(count)

n, s = map(int, input().split())
seq = list(map(int, input().split()))


j = 0
sum = 0
min_length = 100000
start = 0
end = 0
while end <= len(seq):
    if sum >= s:
        min_length = min(min_length, end - start)
        sum -= seq[start]
        start += 1
    else:
        if end == len(seq):
            break
        sum += seq[end]
        end += 1


if min_length == 100000:
    print(0)
else:
    print(min_length)
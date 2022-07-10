str = input()

num = list(map(int, str.replace("-", "+").split("+")))
op = [o for o in str if o == "-" or o == "+"]
minus = False
total = num.pop(0)
while num:
    val = num.pop(0)
    if op and not minus:
        cur_op = op.pop(0)
        if cur_op == "-":
            minus = True

    if minus:
        total -= val
    else:
        total += val
print(total)
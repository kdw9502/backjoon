import sys

input = sys.stdin.readline


a,b,c = map(int, input().split())

mod_dict = dict()
mod_dict[1] = a % c

current_mod = 1
current_exp = 0
cur_b = b
while True:
    cur_divider = 2**current_exp
    if cur_b & 1 == 1:
        current_mod *= mod_dict[cur_divider]
        current_mod %= c

    if cur_b == 0:
        break
    mod_dict[cur_divider * 2] = (mod_dict[cur_divider] ** 2) % c
    cur_b = cur_b // 2
    current_exp += 1


print(current_mod)
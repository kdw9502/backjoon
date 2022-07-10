import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())
pokedex = []
pokedex_dict = dict()
for i in range(N):
    name = input().rstrip()
    pokedex.append(name)
    pokedex_dict[name] = i + 1
for i in range(M):
    question = input().rstrip()
    if question[0].isnumeric():
        print(pokedex[int(question) - 1] + "\n")
    else:
        print(str(pokedex_dict[question])+ "\n")

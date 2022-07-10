import sys
from collections import defaultdict


def input():
    return sys.stdin.readline()

N, M = map(int, input().split())

knows = set(list(map(int, input().split()))[1:])
man_to_party = defaultdict(set)
man_to_man = defaultdict(set)
for i in range(M):
    participates = list(map(int, input().split()))[1:]
    for participate in participates:
        man_to_party[participate].add(i)
        man_to_man[participate].update(participates)



def dfs(current):
    knows.add(current)
    for man in man_to_man[current]:
        if man in knows:
            continue
        dfs(man)
for know in set(knows):
    dfs(know)

no_party = set()
for know in knows:
    no_party.update(man_to_party[know])


print(M - len(no_party))
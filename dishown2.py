import sys
from sys import stdin, stdout

sys.setrecursionlimit(1000000)


def find(a):
    if par[a] == a:
        return a
    else:
        par[a] = find(par[a])
        return par[a]


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if rank[a] > rank[b]:
            par[b] = a
        elif rank[b] > rank[a]:
            par[a] = b
    else:
        stdout.write('Invalid query!\n')


t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    rank = list(map(int, stdin.readline().strip().split(' ')))
    par = [i for i in range(n)]
    q = int(stdin.readline().strip())
    for i in range(q):
        query = list(map(int, stdin.readline().strip().split(' ')));
        if len(query) == 3:
            u, v = query[1] - 1, query[2] - 1
            union(u, v)
        else:
            u = query[1] - 1
            stdout.write(str(find(u) + 1) + "\n")
    del rank, par

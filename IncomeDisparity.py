from collections import defaultdict
from collections import deque
from sys import stdin

dataset = list(map(int, stdin.readline().split(' ')))
no_of_employees = dataset[0]
wealth = dataset[1:no_of_employees + 1]
hierarchy = dataset[no_of_employees + 1:]
boss = 1
graph = defaultdict(set)  # Get rid of duplications
for i in range(no_of_employees):
    if hierarchy[i] == -1:
        boss = i + 1
        continue
    else:
        graph[hierarchy[i]].add(i + 1)


def bfs(boss_, graph_):
    result = -1000000000
    que = deque([])
    que.append(boss_)
    while que:
        key = que.popleft()
        for item in graph_[key]:
            que.append(item)
            z = wealth[key - 1] - wealth[item - 1]
            if result < z:
                result = z
            if wealth[key - 1] > wealth[item - 1]:
                wealth[item - 1] = wealth[key - 1]
    return result


result_ = bfs(boss, graph)
print(result_)

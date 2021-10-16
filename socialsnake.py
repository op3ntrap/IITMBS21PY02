from collections import deque
from sys import stdin

for test_case in range(int(input())):
    rows, columns = map(int, stdin.readline().split(' '))
    income_matrix = []
    for i in range(rows):
        income_matrix.append(list(map(int, stdin.readline().split(' '))))
    max_wealth = 0
    for i in range(rows):
        for j in range(columns):
            max_wealth = max(max_wealth, income_matrix[i][j])
    processing_queue = []
    visited = {}
    for i in range(rows):
        for j in range(columns):
            if income_matrix[i][j] == max_wealth:
                processing_queue.append((i, j))
                visited[(i, j)] = 0
    processing_queue = deque(processing_queue)
    result = 0
    while len(processing_queue) != 0:
        snake = processing_queue.popleft()
        if snake[0] + 1 < rows:
            if (snake[0] + 1, snake[1]) not in visited:
                visited[(snake[0] + 1, snake[1])] = visited[snake] + 1
                processing_queue.append((snake[0] + 1, snake[1]))
            if snake[1] + 1 < columns and (snake[0] + 1, snake[1] + 1) not in visited:
                visited[(snake[0] + 1, snake[1] + 1)] = visited[snake] + 1
                processing_queue.append((snake[0] + 1, snake[1] + 1))
            if snake[1] - 1 >= 0 and (snake[0] + 1, snake[1] - 1) not in visited:
                visited[(snake[0] + 1, snake[1] - 1)] = visited[snake] + 1
                processing_queue.append((snake[0] + 1, snake[1] - 1))
        if snake[0] - 1 >= 0:
            if (snake[0] - 1, snake[1]) not in visited:
                visited[(snake[0] - 1, snake[1])] = visited[snake] + 1
                processing_queue.append((snake[0] - 1, snake[1]))
            if snake[1] + 1 < columns and (snake[0] - 1, snake[1] + 1) not in visited:
                visited[(snake[0] - 1, snake[1] + 1)] = visited[snake] + 1
                processing_queue.append((snake[0] - 1, snake[1] + 1))
            if snake[1] - 1 >= 0 and (snake[0] - 1, snake[1] - 1) not in visited:
                visited[(snake[0] - 1, snake[1] - 1)] = visited[snake] + 1
                processing_queue.append((snake[0] - 1, snake[1] - 1))
        if snake[1] + 1 < columns and (snake[0], snake[1] + 1) not in visited:
            visited[(snake[0], snake[1] + 1)] = visited[snake] + 1
            processing_queue.append((snake[0], snake[1] + 1))
        if snake[1] - 1 >= 0 and (snake[0], snake[1] - 1) not in visited:
            visited[(snake[0], snake[1] - 1)] = visited[snake] + 1
            processing_queue.append((snake[0], snake[1] - 1))
    for i in visited:
        result = max(result, visited[i])
    print(result)

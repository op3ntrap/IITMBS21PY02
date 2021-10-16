import sys
from sys import stdin
from typing import List

sys.setrecursionlimit(10 ** 9)


def is_valid_index(x_: int, y_: int, rows: int, columns: int) -> bool:
    if x_ >= 0 and y_ >= 0:  # indices start from 0,0
        if x_ < rows and y_ < columns:  # indices don't exceed boundaries
            return True
    return False


def connected_lands_nearby(x: int, y: int, grid: List[List[str]]) -> int:
    adjacent_cells = [(x, 1 + y), (x, y - 1), (x + 1, y), (x - 1, y)]  # N,E,W,S of a given cell
    width: int = len(grid)  # rows
    height: int = len(grid[0])  # columns
    if is_valid_index(x, y, width, height) and grid[x][y] == "1":
        grid[x][y] = "0"  # flood the land after acquiring to prevent encroachment
        lands_flooded = 1
        for cell in adjacent_cells:
            crowdx, crowdy = cell
            if is_valid_index(crowdx, crowdy, width, height) and grid[crowdx][crowdy] == "1":
                # Recursively search for nearby lands
                lands_flooded += connected_lands_nearby(crowdx, crowdy, grid)
        return lands_flooded
    else:
        return 0


def codechef_score(grid_: List[List[str]], limit_: int, rows, columns) -> int:
    score_samples = []
    current_score = 0
    chef = 0
    for i in range(rows):
        for j in range(columns):
            if grid_[i][j] == "1":
                possible_score = connected_lands_nearby(i, j, grid_)
                current_score += possible_score
                score_samples.append(possible_score)
            # if current_score == limit_:
    score_samples.sort(reverse=True)
    for count, val in enumerate(score_samples):
        if count % 2 != 0:
            chef += val
    return chef


# Evaluating Case1
final_scores = []
for cases in range(int(input())):
    dim: List[int] = [int(x) for x in stdin.readline().rstrip().split(' ')]
    R: int = dim[0]  # Rows
    C: int = dim[1]  # Cols
    grid_data: List[List[str]] = []
    # No need to search when already flooded all.
    max_score = 0
    for _ in range(R):
        payload = [x for x in stdin.readline().rstrip()]
        grid_data.append(payload)
        max_score += payload.count("1")
    print(codechef_score(grid_data, max_score, R, C))

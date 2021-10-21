from _collections import defaultdict
from sys import stdin

test_cases = int(stdin.readline())
total_cities, total_paths, total_hospitals = tuple(map(int, stdin.readline().split(' ')))

hospitals = {}
paths = defaultdict(dict)
# atlas = {}
# adjacency_list = []
for h_ in range(total_hospitals):
    h_id, cost = tuple(map(int, stdin.readline().split(' ')))
    hospitals[h_id] = cost
# Create all the paths.
for r_ in range(total_paths):
    source, target, distance_cost = tuple(map(int, stdin.readline().split(' ')))
    if source not in paths:
        paths[source][target] = distance_cost
        # atlas[source] = distance_cost

    if target not in paths:
        paths[target][source] = distance_cost

# class City:
#     def __init__(self, city_id, hospital_id=None, neighbours=None):
#         self.id = city_id

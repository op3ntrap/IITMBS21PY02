import sys
from random import randint, choice
from typing import List, Dict


class Dish:
    def __init__(self, _id, _score):
        self.id: int = _id
        self.score: int = _score
        self.owner: int = _id


def find_root(_dish_id: int, table) -> int:
    given_dish = table[_dish_id]
    if given_dish.owner == _dish_id:
        return given_dish.owner
    else:
        given_dish.owner = find_root(given_dish.owner, table)
        return given_dish.owner


def compete(_dish_x, _dish_y, table):
    _dx_root, _dy_root = find_root(_dish_x, table), find_root(_dish_y, table)
    if _dx_root == _dy_root:
        print("Invalid query!")
        return
    else:
        rx: Dish = table[_dx_root]
        ry: Dish = table[_dy_root]
        if rx.score > ry.score:
            ry.owner = rx.id
        if rx.score < ry.score:
            rx.owner = ry.id


def print_owner(_dish, table):
    print(find_root(_dish, table))


for test_cases in range(int(sys.stdin.readline())):
    size = int(sys.stdin.readline())
    _scores = list(map(int, sys.stdin.readline().split(' ')))
    _table = {x: Dish(x, _scores[x - 1]) for x in range(1, size + 1)}
    for queries in range(int(sys.stdin.readline())):
        query = list(map(int, sys.stdin.readline().split(' ')))
        if query[0] == 0:
            compete(query[1], query[2], table=_table)
        if query[0] == 1:
            print_owner(query[1], table=_table)

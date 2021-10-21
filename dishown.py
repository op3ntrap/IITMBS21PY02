from random import randint
from typing import List, Dict


class Dish:
    def __init__(self, _id, _score=None, parent=None):
        self.id: int = _id
        self.score: int = _score
        self.owner: int = parent


size = 10 ** 4
_scores: List[int] = [randint(10000, 90000)] * size
table = {x: Dish(x, _scores[x - 1], parent=x) for x in range(1, size + 1)}


# dishes = [D]
# Test
def find_root(_dish_id: int) -> int:

#
# class Dishes:
#     def __init__(self, size, scores):
#         self.size: int = size
#         self.scores: List[int] = scores
#         # self.table: Dict[int, Dish] = {}
#         self.table = {x: Dish(x, self.scores[x - 1], parent=x) for x in range(1, self.size + 1)}
#
#     def data(self):

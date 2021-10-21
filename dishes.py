import sys


class Dish:
    def __init__(self, _id, score):
        self.owner = None
        self.score = score
        self.id = _id


class Dishes:
    def __init__(self, size, scores):
        self.size = size
        self.data = {}
        for i in range(1, size + 1):
            self.data[i] = Dish(i, scores[i - 1])


# class Chef:
#     def __init__(self, idx, initial_score):
#         self.dish = idx


class Chef:
    def __init__(self, _id):
        self.id = _id
        self.dish = []
        self.max_score = None


class Chefs:
    def __init__(self, size, _Dishes):
        self.size = size
        self.dishes = _Dishes.data
        self.table = {}
        for i in range(1, size + 1):
            self.table[i] = Chef(i)
            my_chef = self.table[i]
            my_chef.dish.append(self.dishes[i])
            my_chef.max_score = self.dishes[i].score
            self.dishes[i].owner = my_chef
        # self.max_score = self.dishes[i].score

    def compete(self, x, y):
        a = self.dishes[x].owner
        b = self.dishes[y].owner
        if a == b:
            return sys.stdout.write("Invalid query!")
        if a.max_score < b.max_score:
            # transfer ownership
            # self.dishes[x].owner = b
            for __d in a.dish:
                __d.owner = b
                b.dish.append(__d)

            # eliminate candidate
            # loser = a
            del self.table[a.id]

        elif a.max_score > b.max_score:
            # transfer ownership
            # self.dishes[y].owner = a
            for __d in b.dish:
                __d.owner = a
                a.dish.append(__d)
            # eliminate candidate
            # loser = b
            del self.table[b.id]

    def get_owner(self, dish_id):
        print(self.dishes[dish_id].owner.id)
        # return sys.stdout.write(self.dishes[dish_id].owner.id)


# init_dishes = Dishes(_size, _scores)
# chefs = Chefs(_size, init_dishes)
def main():
    for test_cases in range(int(sys.stdin.readline())):
        _size = int(sys.stdin.readline())
        _scores = list(map(int, sys.stdin.readline().split(' ')))
        # init_dishes = Dishes(_size, _scores)
        # chefs = Chefs(_size, init_dishes)
        for queries in range(int(sys.stdin.readline())):
            query = list(map(int, sys.stdin.readline().split(' ')))
            if query[0] == 0:
                # chefs.compete(query[1], query[2])
                pass
            if query[0] == 1:
                # chefs.get_owner(query[1])
                pass


if __name__ == '__main__':
    main()

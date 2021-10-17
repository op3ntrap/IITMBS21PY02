from sys import stdin


class GFATeam:
    def __init__(self, value: int, rank: int, cost: int):
        self.id: int = value
        self.rank = rank
        self.cost = cost
        # initialise each team's roots as themselves
        self.root: GFATeam = self


class GFA:
    def __init__(self, members, agreements):
        custom_range = range(1, members + 1)
        self.directory: dict[int, GFATeam] = {
            i: GFATeam(i, 0, -1) for i in custom_range
        }
        self.planets = members
        self.pathways = agreements
        self.efficient_path = set()
        self.minimum_cost = None

    def fetch_root(self, team: int):
        # if root of a team is still itself
        team_instance = self.directory[team]
        if team_instance.root == team_instance:
            return team_instance  # return team.root
        else:
            team_instance.root = self.fetch_root(self.directory[team].root.id)  # recursive search
            return team_instance.root

    def union(self, source_id: int, target_id: int):
        parent_source, target_source = self.fetch_root(source_id), self.fetch_root(target_id)
        if parent_source != target_source:
            if parent_source.rank > target_source.rank:
                target_source.root = parent_source
            elif parent_source.rank < target_source.rank:
                parent_source.root = target_source
            else:
                parent_source.root = target_source
                target_source.rank += 1

    def process_existing_paths(self):
        for path_ in range(self.pathways):
            source, target = tuple(map(int, stdin.readline().split(' ')))
            self.union(source, target)

    def update_cost_indices(self):
        for planet in range(1, self.planets + 1):
            given_cost = int(stdin.readline())
            planet_root = self.fetch_root(planet)
            self.efficient_path.add(planet_root)
            if given_cost >= 0:
                if planet_root.cost == -1:
                    planet_root.cost = given_cost
                else:
                    planet_root.cost = min(planet_root.cost, given_cost)

    def is_viable(self):
        # flag = False
        if len(self.efficient_path) == 1:
            self.minimum_cost = 0
            return True
        else:
            for p_ in self.efficient_path:
                if p_.cost == -1:
                    self.minimum_cost = -1
                    return False
                    # break
        return True

    def minimum_viable_cost(self):
        if self.is_viable():
            costs = [planet.cost for planet in self.efficient_path]
            costs.sort()
            self.minimum_cost = sum(costs) + (len(self.efficient_path) - 2) * costs[0]
        return self.minimum_cost

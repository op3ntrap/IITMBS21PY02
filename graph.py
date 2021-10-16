# import graph


class Node:
    def __init__(self, value, priority, rank):
        self.__value__ = value
        self.priority = priority
        self.rank = rank
        self.incoming = []
        self.outgoing = []
        self.parent = None
        self.child = None
        self.in_degree = len(self.incoming)
        self.out_degree = len(self.outgoing)


class Edge:
    def __init__(self, source=None, target=None, weight=None):
        self.source = source
        self.target = target
        self.weight = weight


class Graph:
    """
    Graph Standard Library for all problems.
    """

    def __init__(self, adjlist=False, nodes=0, edges=0):
        if adjlist is True:
            self.adjList = None
        self.edges = []
        self.nodes = []
        # if nodes != 0:
        #     self.nodes: list = [Node(None, None, 0) for x in range(nodes)]
        #     # self.nodes = nodes
        # if edges != 0:
        #     self.edges = [Edge(None, None, 0) for x in range(edges)]
        #     # self.edges = edges

    def incoming(self, node):
        for node in self.nodes:
            node.incoming_edges = [x[0] for x in self.edges]

    def outgoing(self, node):
        node.outgoing_edges = [x[1] for x in self.edges]

    @staticmethod
    def is_adjacent(node1, node2):
        if (node2 in node1.outgoing_edges) or (node1 in node2.incoming_edges):
            return True
        return False

    def op(self):
        pass

    def initial_setup(self):
        pass

"""
Breadth-First Search algorithm runs on unweighted graphs.

Complexity of the BFS is O(V + E), where V is the number of vertices, and E is the number of Edges.
"""
from collections import deque


def bfs(name):
    search_queue = deque()
    search_queue.extend(graph[name])
    searched = []
    while search_queue:
        if (person := search_queue.popleft()) not in searched:
            if is_seller(person):
                return person
            else:
                search_queue.extend(graph[person])
                searched.append(person)
    return None


def is_seller(person):
    return person[-1] == 'm'


# Test data.
graph = {
    'you': ['alice', 'bob', 'claire'],
    'alice': ['peggy'],
    'bob': ['anuj', 'peggy'],
    'claire': ['john', 'thom'],
    'anuj': [],
    'john': [],
    'peggy': [],
    'thom': [],
}

# Test breadth-first search algorithm.
print(bfs('you'))    # thom
print(bfs('peggy'))  # None

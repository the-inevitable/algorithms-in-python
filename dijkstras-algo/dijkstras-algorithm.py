"""
In Dijkstra’s algorithm, you assign a number or weight to each segment.
Then Dijkstra’s algorithm finds the path with the smallest total weight.

Dijkstra’s algorithm only works with directed acyclic graphs, called DAGs for short.

The algorithm runs only on weighted graphs.

You can’t use Dijkstra’s algorithm if you have negative-weight edges.

If you want to find the shortest path in a graph that has negative-weight edges,
there’s the Bellman-Ford algorithm for that.

Algorithm pseudo code:

1. While we have nodes to process
2. Grab the node that is closest (cheapest, lightest) to the start.
3. Update costs for its neighbours.
4. If any of the neighbours' costs were updated , update the parents too.
5. Mark this node processed.
"""


# Graph modelling.
graph = {}

graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2

graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7

graph['c'] = {}
graph['c']['finish'] = 3
graph['c']['d'] = 6

graph['d'] = {}
graph['d']['finish'] = 1

graph['finish'] = {}


# Modelling the "edge costs" (weight) graph.
infinity = float('inf')

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['finish'] = infinity


# Modelling the nodes' parents graph.
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['finish'] = None


# A structure to keep track of processed nodes
# as we don't want to process the same node more than once.
processed = []


# Implementation.
def find_lowest_cost_node(dct):
    current_lowest = float('inf')
    lowest_cost_node = None
    for node in costs:
        if (cost := costs[node]) < current_lowest and node not in processed:
            current_lowest = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstras_algo():
    while node := find_lowest_cost_node(costs):
        cost = costs[node]
        neighbours = graph[node]
        for key in neighbours.keys():
            if costs[key] > (new_cost := cost + neighbours[key]):
                costs[key] = new_cost
                parents[key] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


def compose_shortest_path(dct):
    steps = ['finish']
    node = dct['finish']
    while node:
        steps.append(node)
        if node == 'start':
            break
        node = dct[node]
    return reversed(steps)


# Test the Dijkstra's algorithm.
dijkstras_algo()
print(' --> '.join(compose_shortest_path(parents)))  # start --> a --> d --> finish


from dsc40graph import UndirectedGraph
from typing import Dict, Callable, Any, FrozenSet
from collections import deque

def cluster(graph: UndirectedGraph, weights: Callable[[Any, Any], float], level: float) -> FrozenSet[FrozenSet[Any]]:
    """
    Computes the clusters of a weighted graph at a given level.

    Parameters
    ----------
    graph : UndirectedGraph
        Graph of type UndirectedGraph from the dsc40graph package.
    weights : Callable[[Any, Any], float]
        A function returning the weight of an edge between two nodes.
    level : float
        The level at which to find the clusters.

    Returns
    -------
    clusters : Tuple
        The clusters of the graph at the given level.

    # Doctests

    # Test a graph with edges of varying weights.
    # The output when run with a level of 0.4 should be:
    >>> def weights(x, y):
    ...     x, y = (x, y) if x < y else (y, x)
    ...     return {("a", "b"): 1, ("b", "c"): .3, ("c", "d"): .9, ("a", "d"): .2}[(x, y)]
    >>> g = UndirectedGraph()
    >>> g.add_edge('a', 'b')
    >>> g.add_edge('b', 'c')
    >>> g.add_edge('c', 'd')
    >>> g.add_edge('a', 'd')
    >>> cluster(g, weights, 0.4)
    (['a', 'b'], ['c', 'd'])

    # Test a graph with edges of varying weights.
    # The output when run with a level of 0.4 should be:
    >>> def weights(x, y):
    ...     x, y = (x, y) if x < y else (y, x)
    ...     return {("a", "b"): 1, ("b", "c"): .3, ("c", "d"): .9, ("a", "d"): .2}[(x, y)]
    >>> g = UndirectedGraph()
    >>> g.add_edge('a', 'b')
    >>> g.add_edge('b', 'c')
    >>> g.add_edge('c', 'd')
    >>> g.add_edge('a', 'd')
    >>> cluster(g, weights, 0.4)
    (['a', 'b'], ['c', 'd'])

    # Test a graph where all edges have the same weight.
    # The output should be one cluster containing all nodes if the level is less than the weight,
    # and separate clusters for each node if the level is greater than the weight.
    >>> def weights(x, y):
    ...     return 1
    >>> g = UndirectedGraph()
    >>> g.add_edge('a', 'b')
    >>> g.add_edge('b', 'c')
    >>> g.add_edge('c', 'd')
    >>> g.add_edge('a', 'd')
    >>> cluster(g, weights, 0.5)
    (['a', 'b', 'c', 'd'])
    >>> cluster(g, weights, 1.5)
    (['a'], ['b'], ['c'], ['d'])

    # Test an empty graph.
    # The output should be an empty tuple since there are no nodes.
    >>> def weights(x, y):
    ...     return 1
    >>> g = UndirectedGraph()
    >>> cluster(g, weights, 1)
    ()

    # Test a graph with one node and no edges.
    # The output should be a single cluster containing the one node, regardless of the level.
    >>> def weights(x, y):
    ...     return 1
    >>> g = UndirectedGraph()
    >>> g.add_node('a')
    >>> cluster(g, weights, 1)
    (['a'])

    # Test a graph with two nodes and an edge between them.
    # The output should be one cluster containing both nodes if the level is less than the weight,
    # and separate clusters for each node if the level is greater than the weight.
    >>> def weights(x, y):
    ...     return 1
    >>> g = UndirectedGraph()
    >>> g.add_edge('a', 'b')
    >>> cluster(g, weights, 0.5)
    (['a', 'b'])
    >>> cluster(g, weights, 1.5)
    (['a'], ['b'])
    """
    visited = set()
    clusters = set()

    for node in graph.nodes:
        if node not in visited:
            current_cluster = set()
            queue = deque([node])
            while queue:
                current_node = queue.popleft()
                if current_node not in visited:
                    visited.add(current_node)
                    current_cluster.add(current_node)
                    for neighbor in graph.neighbors(current_node):
                        if weights(current_node, neighbor) >= level:
                            queue.append(neighbor)
            clusters.add(frozenset(current_cluster))

    return frozenset(clusters)

    def dfs(node, current_cluster):
        visited.add(node)
        current_cluster.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited and weights(node, neighbor) >= level:
                dfs(neighbor, current_cluster)

    visited = set()
    clusters = set()

    for node in graph.nodes:
        if node not in visited:
            current_cluster = set()
            dfs(node, current_cluster)
            clusters.add(frozenset(current_cluster))

    return frozenset(clusters)

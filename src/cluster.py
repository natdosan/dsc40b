from dsc40graph import UndirectedGraph
from typing import Callable, Any, List, Tuple

def cluster(graph: UndirectedGraph, weights: Callable[[Any, Any], float], level: float) -> Tuple:
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

    def dfs(node, cluster):
        visited[node] = True
        cluster.append(node)
        for neighbor in graph.neighbors(node):
            if weights(node, neighbor) >= level and not visited[neighbor]:
                dfs(neighbor, cluster)
    
    visited = {node: False for node in graph.nodes}
    clusters = []

    for node in graph.nodes:
        if not visited[node]:
            current_cluster = []
            dfs(node, current_cluster)
            clusters.append(current_cluster)
    
    return tuple(clusters)
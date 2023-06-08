from dsc40graph import UndirectedGraph
from disjoint_set_forest import DisjointSetForest
from operator import itemgetter


def slc(graph, d, k):
    """
    Perform single linkage clustering using Kruskal’s algorithm

    Parameters
    ----------
    graph : dsc40graph.UndirectedGraph
        input graph, G = (V, E)
    d : func
        of two arguments which takes in two nodes and returns the distance (or dissimilarity)
    k : int
        positive integer describing the number of clusters which should be found

    Returns
    -------
    frozenset : of k frozensets, each representing a cluster of the graph.
    
    >>> import dsc40graph
    >>> g = dsc40graph.UndirectedGraph()
    >>> edges = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'd')]
    >>> for edge in edges: g.add_edge(*edge)
    >>> def d(edge):
    ...     u, v = sorted(edge)
    ...     return {
    ...         ('a', 'b'): 1,
    ...         ('a', 'c'): 4,
    ...         ('b', 'd'): 3,
    ...         ('c', 'd'): 2,
    ...     }[(u, v)]
    >>> slc(g, d, 2) == frozenset({frozenset({'a', 'b'}), frozenset({'c', 'd'})})
    True

    # Edge case: when there are no edges in the graph
    >>> g = dsc40graph.UndirectedGraph()
    >>> slc(g, d, 2) == frozenset()
    True

    # Edge case: when there is only one node in the graph
    >>> g = dsc40graph.UndirectedGraph()
    >>> g.add_node('a')
    >>> slc(g, d, 1) == frozenset({frozenset({'a'})})
    True

    # Edge case: when k is greater than the number of nodes in the graph
    >>> g = dsc40graph.UndirectedGraph()
    >>> edges = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'd')]
    >>> for edge in edges: g.add_edge(*edge)
    >>> slc(g, d, 5) == frozenset({frozenset({'a'}), frozenset({'b'}), frozenset({'c'}), frozenset({'d'})})
    True
    """

    # Create a disjoint set forest with the graph's nodes
    dsf = DisjointSetForest(graph.nodes)

    # Create sorted list of all edges in the graph, along with their weights
    # where an edge is represented as a tuple (weight, node1, node2)
    edges = [(d(edge), *edge) for edge in graph.edges]
    edges.sort()

    # Keep joining edges with the smallest weights using the 
    # disjoint set forest until the number of clusters equals k
    while len(set(dsf.find_set(node) for node in graph.nodes)) > k:
        _, u, v = edges.pop(0)
        if not dsf.in_same_set(u, v):
            dsf.union(u, v)

    # Gather all nodes belonging to the same set in the disjoint set forest
    clusters = {}
    for node in graph.nodes:
        set_representative = dsf.find_set(node)
        if set_representative not in clusters:
            clusters[set_representative] = set()
        clusters[set_representative].add(node)

    return frozenset(frozenset(cluster) for cluster in clusters.values())

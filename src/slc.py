from dsc40graph import UndirectedGraph
from disjoint_set_forest import DisjointSetForest

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

    # 1. sort in ascending order by distance
    sorted_edges = sorted(graph.edges, key=d)

    # 2. create a DisjointSetForest to keep track of the clusters
    dsf = DisjointSetForest(graph.nodes)

    # 3. Initialize an empty set to store the edges that form the MST
    C = set()

    # 4. Go through all edges in sorted order
    for edge in sorted_edges:
        u, v = sorted(edge)

        # 5. If adding this edge does not form a cycle (i.e., u and v are not in the same set)
        if not dsf.in_same_set(u, v):
            # 6. Add this edge to the MST
            C.add(frozenset([u, v]))
            # 7. Merge the two sets in the DisjointSetForest
            dsf.union(u, v)

    # 8. Until there are k clusters, find the longest edge in the MST and remove it
    while len(C) > k-1:
        longest_edge = max(C, key=d)
        C.remove(longest_edge)

    # 9. Now, each set in the DisjointSetForest represents a cluster, 
    # thus we return a frozenset of these clusters
    print(frozenset(map(frozenset, (dsf.find_set(node) for node in graph.nodes))))
    return frozenset(map(frozenset, (dsf.find_set(node) for node in graph.nodes)))

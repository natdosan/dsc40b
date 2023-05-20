from dsc40graph import DirectedGraph
from typing import Dict, Any

def biggest_descendent(graph: DirectedGraph, root: Any, value: Dict[Any, int]) -> Dict[Any, int]:
    """
    Finds the biggest descendent value for each node in the graph.

    Example:
    >>> edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]
    >>> g = DirectedGraph()
    >>> for edge in edges: g.add_edge(*edge)
    >>> value = {1: 2, 2: 1, 3: 4, 4: 8, 5: 5, 6: 2, 7: 10, 8:3, 9: 9}
    >>> biggest_descendent(g, 1, value)
    {1: 10, 2: 9, 3: 10:, 4: 9, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}

    Parameters
    ----------
    graph : DirectedGraph
        Graph of type DirectedGraph from the data100graph package.
    root : Any
        The root node of the tree.
    value : Dict[Any, int]
        A dictionary mapping each node in the graph to an integer.

    Returns
    -------
    biggest_values : Dict[Any, int]
        A dictionary mapping each node in the graph to the biggest descendent value.
    """
    biggest_values = {}
    
    def dfs(node):
        biggest_values[node] = value[node]
        for child in graph.neighbors(node):
            dfs(child)
            biggest_values[node] = max(biggest_values[node], biggest_values[child])
    
    dfs(root)
    return biggest_values
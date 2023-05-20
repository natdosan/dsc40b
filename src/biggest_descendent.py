from dsc40graph import DirectedGraph
from typing import Dict, Any

def biggest_descendent(graph: DirectedGraph, root: Any, value: Dict[Any, int]) -> Dict[Any, int]:
    """
    Finds the biggest descendent value for each node in the graph.

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

    Example:
    >>> edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]
    >>> g = DirectedGraph()
    >>> for edge in edges: g.add_edge(*edge)
    >>> value = {1: 2, 2: 1, 3: 4, 4: 8, 5: 5, 6: 2, 7: 10, 8:3, 9: 9}
    >>> biggest_descendent(g, 1, value)
    {1: 10, 2: 9, 3: 10:, 4: 9, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}

    # Test a graph where all nodes have the same value.
    # The output should have the same value for all nodes. 
    >>> edges = [(1, 2), (1, 3), (2, 4), (3, 5)]
    >>> g = DirectedGraph()
    >>> for edge in edges: g.add_edge(*edge)
    >>> value = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}
    >>> biggest_descendent(g, 1, value)
    {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}

    # Test a linear graph where the values are decreasing. 
    # The maximum descendant value should decrease along the path.
    >>> edges = [(1, 2), (2, 3), (3, 4)]
    >>> g = DirectedGraph()
    >>> for edge in edges: g.add_edge(*edge)
    >>> value = {1: 4, 2: 3, 3: 2, 4: 1}
    >>> biggest_descendent(g, 1, value)
    {1: 4, 2: 3, 3: 2, 4: 1}

    # Test a linear graph where the values are increasing. 
    # The maximum descendant value should remain the root value until the last node.
    >>> edges = [(1, 2), (2, 3), (3, 4)]
    >>> g = DirectedGraph()
    >>> for edge in edges: g.add_edge(*edge)
    >>> value = {1: 1, 2: 2, 3: 3, 4: 4}
    >>> biggest_descendent(g, 1, value)
    {1: 4, 2: 4, 3: 4, 4: 4}
    """
    biggest_values = {}
    
    def dfs(node):
        biggest_values[node] = value[node]
        for child in graph.neighbors(node):
            dfs(child)
            biggest_values[node] = max(biggest_values[node], biggest_values[child])
    
    dfs(root)
    return biggest_values
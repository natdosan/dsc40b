from dsc40graph import UndirectedGraph
from typing import Dict, Optional

def assign_good_and_evil(graph: UndirectedGraph) -> Optional[Dict[str, str]]:
    """
    Determines if it is possible to label each university as either “good” or 
    “evil” such that every rivalry is between a “good” school and an “evil” 
    school. 
    
    Parameters
    ----------
    graph : UndirectedGraph
        graph of type UndirectedGraph from the dsc40graph package.
         
    Returns
    -------
    labels : dict
        If there is a way to label each node as “good” and “evil” so that 
        every rivaly is between a “good” school and an “evil” school, return 
        it as a dictionary mapping each node to a string, 'good' or 'evil'; 
        if such a labeling is not possible, return None

    # Doctests

    >>> example_graph = UndirectedGraph()
    >>> example_graph.add_edge('Michigan', 'OSU')
    >>> example_graph.add_edge('USC', 'OSU')
    >>> example_graph.add_edge('USC', 'UCB')
    >>> example_graph.add_node('UCSD')
    >>> assign_good_and_evil(example_graph)
    {'OSU': 'good', 'Michigan': 'evil', 'USC': 'evil', 'UCB': 'good', 'UCSD': 'good'}
    """
    labels = {}
    for node in graph.nodes:
        if node not in labels:
            stack = [(node, 'good')]
            while stack:
                node, label = stack.pop()
                if node in labels:
                    if labels[node] != label:
                        return None
                else:
                    labels[node] = label
                    for neighbor in graph.neighbors(node):
                        stack.append((neighbor, 'evil' if label == 'good' else 'good'))
    return labels







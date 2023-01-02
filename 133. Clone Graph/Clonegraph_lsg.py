from collections import deque, defaultdict
from copy import deepcopy
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # return deepcopy(node)
        if not node:
            return None

        adj = dict()
        dq = deque([node])
        while dq:
            ref = dq.popleft()
            val = ref.val
            if not val in adj:
                adj[val] = [n.val for n in ref.neighbors]
                dq.extend(ref.neighbors)

        deepcopy_node = dict()
        for i in adj.keys():
            deepcopy_node[i] = Node(i)
        for i in adj.keys():
            deepcopy_node[i].neighbors = [deepcopy_node[n] for n in adj[i]]

        return deepcopy_node[1]

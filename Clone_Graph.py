# Leetcode - 133. Clone Graph
# hhttps://leetcode.com/problems/clone-graph
# Deep Copy of Undirected Cyclic Graph

# DFS Approach 
# Time Complexity - O(V+E)
# Space Complexity - O(V)
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        hash_map = {}

        def traverse(root):
            if root.val not in hash_map:
                temp_node = Node(root.val)
                hash_map[root.val]=temp_node
                temp_neighbors = []
                for neighbor in root.neighbors:
                    temp_neighbors+=[traverse(neighbor)]
                temp_node.neighbors = temp_neighbors
            return hash_map[root.val]
        
        return traverse(node) if node else node

# BFS Approach
# Time Complexity - O(V+E)
# Space Complexity - O(V)
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        root = None
        if node:
            hash_map = {}
            queue = deque()
            hash_map[node.val] = root = Node(node.val)
            queue.append(node)
            while queue:
                main_node = queue.popleft()
                clone_node = hash_map[main_node.val]
                neighbors = []
                for neighbor in main_node.neighbors:
                    if neighbor.val not in hash_map:
                        queue.append(neighbor)
                        hash_map[neighbor.val] = Node(neighbor.val)
                    neighbors+=[hash_map[neighbor.val]]
                clone_node.neighbors = neighbors
        return root
                
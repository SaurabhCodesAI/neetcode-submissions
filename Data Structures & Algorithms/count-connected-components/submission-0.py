class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n
        count = n
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False
            if size[root1] >= size[root2]:
                parent[root2] = root1
                size[root2] += size[root1]
            else:
                parent[root1] = root2
                size[root1] += size[root2]
            return True
        for node1, node2 in edges:
            if union(node1, node2):
                count -= 1
        return count
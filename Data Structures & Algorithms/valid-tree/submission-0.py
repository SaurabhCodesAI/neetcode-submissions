class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for nxt in graph[node]:
                if nxt == parent:
                    continue

                if not dfs(nxt, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
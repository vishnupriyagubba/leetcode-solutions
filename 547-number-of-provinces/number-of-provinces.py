class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(city):
            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        p = 0
        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                p+=1
        return p

        
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,price in flights:
            graph[u].append((v,price))
        q= deque()
        q.append((src,0,0))
        dist = [float('inf')]*n
        dist[src]=0
        while q:
            node,cost,stops = q.popleft()
            if stops > k:
                continue
            for nei,price in graph[node]:
                new_cost = cost+price
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    q.append((nei,new_cost,stops+1))
        return dist[dst] if dist[dst] != float('inf') else -1
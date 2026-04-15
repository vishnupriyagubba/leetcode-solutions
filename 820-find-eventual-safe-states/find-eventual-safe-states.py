class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #dfs
        """n=len(graph)
        v=[0]*n
        pv=[0]*n
        check=[0]*n
        def dfs(node):
            v[node]=1
            pv[node]=1
            for nei in graph[node]:
                if v[nei]==0:
                    if dfs(nei):
                        return True
                elif pv[nei]==1:
                    return True
            check[node]=1
            pv[node]=0
            return False
        for i in range(n):
            if v[i]==0:
                dfs(i)
        safe=[]
        for i in range(n):
            if check[i]==1:
                safe.append(i)
        return safe"""
        #bfs
        """n=len(graph)
        out=[0]*n
        revg=[[]for i in range(n)]
        for u in range(n):
            out[u]=len(graph[u])
            for v in graph[u]:
                revg[v].append(u)
        q=[]
        for i in range(n):
            if out[i]==0:
                q.append(i)
        safe=[False]*n
        while q:
            node=q.pop(0)
            safe[node]=True
            for prev in revg[node]:
                out[prev]-=1
                if out[prev]==0:
                    q.append(prev)
        res=[]
        for i in range(n):
            if safe[i]:
                res.append(i)
        return res"""
        n=len(graph)
        states=[0]*n
        def dfs(node):
            if states[node]!=0:
                return states[node]==2
            states[node]=1
            for nei in graph[node]:
                if states[nei]==1 or not dfs(nei):
                    return False
            states[node]=2
            return True
        res=[]
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
                





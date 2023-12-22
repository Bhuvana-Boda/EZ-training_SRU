---->dfs
* dfs uses stack
* we use recursion for dfs
---->bellman's ford
*it uses dynamic programming approach
----------------------------------------------------------------------------
:::::>dfs

def dfs(start,visited):
    visited.add(start)
    for i in d[start]:
        if i not in visited:
            dfs[i,visited]
-----------------------------------------------------------------------------
:::::>1971)find if the path exists in the graph or not using dfs

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        d={i: [] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        vis=set()
        def dfs(start,vis):
            vis.add(start)
            if start==destination:
                return True
            for i in d[start]:
                if i not in vis:
                    if dfs(i,vis):
                        return True
        return dfs(source,vis)
----------------------------------------------------------------------------
:::::>797)all paths from source to target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        def dfs(start,end,visited):
            if start==end:
                val=visited+[start]
                ans.append(val)
                return
            visited.append(start)
            for i in graph[start]:
                if i not in visited:
                    dfs(i,end,visited)
            visited.pop()
        dfs(0,len(graph)-1,[])
        return ans
---------------------------------------------------------------------------
:::::>to find whether cycle is present in graph or not

def dfs(start,vis):
    vis.add(start)
    for i in d[start]:
        if i in vis:
            return True
        else:
            if dfs(i,vis):
                return False
    for i in d:
        if dfs(i,[]):
            return True
-----------------------------------------------------------------------------
:::::>787)cheapest flights with k stops


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]=0
        for i in range(k+1):
            temp=prices.copy()
            for s,d,w in flights:
                if prices[s]!=float("inf") and prices[s]+w<temp[d]:
                    temp[d]=prices[s]+w
            prices=temp
        return -1 if prices[dst]==float("inf") else prices[dst]
----------------------------------------------------------------------------
:::::>841)keys and rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=set()
        def dfs(start):
            vis.add(start)
            for i in rooms[start]:
                if i not in vis:
                    dfs(i)
        dfs(0)
        return True if len(vis)==len(rooms) else False


















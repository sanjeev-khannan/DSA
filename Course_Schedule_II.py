# Leetcode - 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii

# Disconnected graph traversal using DFS

# DFS Approach 
# Time Complexity - O(V+E)
# Space Complexity - O(V)
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

    graph = defaultdict(list)

    for a, b in prerequisites:
        graph[b]+=[a]

    path = [False]*numCourses
    seen = [False]*numCourses
    order = []
    
    def traverse(node):
        nonlocal order
        if not seen[node]:
            if path[node]:
                return False
            path[node]=True
            for child in graph[node]:
                if not traverse(child):
                    return False
            path[node]=False
            seen[node]=True
            order = [node] + order
        return True
    
    for i in range(numCourses):
        if not seen[i]:
            if not traverse(i):
                return []
    return order

# BFS Approach 
# Time Complexity - O(V+E)
# Space Complexity - O(V)
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

    graph = defaultdict(list)
    indegree = [0]*numCourses

    for b, a in prerequisites:
        graph[a] += [b]
        indegree[b]+=1
    
    queue = deque()
    order = []
    
    for i in range(numCourses):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        numCourses-=1
        order+=[node]
        for child in graph[node]:
            indegree[child]-=1
            if indegree[child]==0:
                queue.append(child)
    
    return order if numCourses==0 else []

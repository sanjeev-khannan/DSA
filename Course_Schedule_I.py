# Leetcode - 207. Course Schedule
# https://leetcode.com/problems/course-schedule
# Disconnected Graph Traversal

# DFS Approach
# Time complexity - O(V+E)
# Space complexity - O(V)
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
    graph = defaultdict(list)

    for a, b in prerequisites:
        graph[b]+=[a]
    
    path=[False]*numCourses
    seen=[False]*numCourses
    
    def traverse(node):
        if not seen[node]:
            if path[node]:
                return False
            path[node] = True
            for child in graph[node]:
                if not traverse(child):
                    return False
            seen[node] = True
            path[node] = False
        return True
    
    for i in range(numCourses):
        if not seen[i]:
            if not traverse(i):
                return False
    return True

# BFS Approach
# Time complexity - O(V+E)
# Space complexity - O(V)
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
    graph = defaultdict(list)
    indegree = [0]*numCourses
    
    for a, b in prerequisites:
        graph[b]+=[a]
        indegree[a]+=1

    queue = deque()
    for i in range(numCourses):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        numCourses-=1
        for child in graph[node]:
            indegree[child]-=1
            if indegree[child]==0:
                queue.append(child)

    return numCourses==0

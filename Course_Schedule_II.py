# Leetcode - 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii

# Disconnected graph traversal using DFS

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

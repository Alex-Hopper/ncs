class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        # build graph
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def done(cr, visited) -> bool:
            if cr in visited:
                return False
            visited.add(cr)
            graph[cr] = [c for c in graph[cr] if not done(c, visited)]
            visited.remove(cr)
            return len(graph[cr]) == 0

        for i in range(numCourses):
            if not done(i, set()):
                return False
                
        return True

        
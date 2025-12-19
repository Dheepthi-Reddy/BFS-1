'''
Given an array of courses and its prerequisites, we have to return if we can finish all the courses or not.
To finish all the courses, we first have to start with a course that has no prerequisites, store that in a queue.
We can store the count of each course dependencies in a indegree array, to get the order of the prerequisites.
As soon as we are done with the independent course we can pop the course and add the courses which are dependent on this, parallaly we update the counts in indegree array.
inorder not to iterate on the tree everytime for going through the courses, we can maintain the adjecency map to store the independent courses as keys and dependent course arrays as values
we update the queue and indegree for every iteration, if length of queue becomes equal to the no of courses, we are finished with all the courses.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = {}

        for p in prerequisites:
            # incrasing indegree of dependent course
            indegrees[p[0]] += 1
            # mapping courses to its prerequisites
            if p[1] not in graph:
                graph[p[1]] = []
            graph[p[1]].append(p[0])
        
        count = 0
        q = deque()

        # iterating on courses
        for i in range(numCourses):
            # whichever course indegree is 0 is added to queue
            if indegrees[i] == 0:
                q.append(i)
                count += 1

        if not q:
            return False
        if count == numCourses:
            return True
        
        while q:
            # popping the first course
            curr = q.popleft()
            # getting dependent courses existing on the popped course
            children = graph.get(curr)
            # checking if it has any children to iterate
            if children:
                for child in children:
                    # reducing indegrees count
                    indegrees[child] -= 1
                    # if its zero add to the queue
                    if indegrees[child] == 0:
                        q.append(child)
                        count += 1
                        if count == numCourses:
                            return True
        return False
'''
Time Complexity: O(V+E)
maximum time taken is the no of courses and number of edges
Space Complexity: O(V+E)
space consumed by the indegrees array is V and by the map is E
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()
        output = []

        def dfs(crs):
            if crs in visit:
                return False
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            # ✅ mark processed
            preMap[crs] = []
            # ✅ append *every* course once processed
            if crs not in output:
                output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output

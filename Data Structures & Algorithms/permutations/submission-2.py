class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       
        res = []
        path = []
        used = [False] * len(nums)   # track used numbers

        def backtrack():
            if len(path) == len(nums):      # base case
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:                 # skip if already used
                    continue

            # 1. Choose
                path.append(nums[i])
                used[i] = True

            # 2. Recurse
                backtrack()

            # 3. Undo
                path.pop()
                used[i] = False

        backtrack()
        return res

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        x = len(nums)
        result = max(self.helper (nums[:x-1]), self.helper(nums[1:]))

        return result



    def helper (self, nums) :
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        res = [0]* n 
        res [0] = nums [0]
        res [ 1 ] =max(nums [0], nums[1])

        for i in range(2, n): 
            res [i] = max(res[i-1], res [i-2]+ nums[i])
            
        return max(res [n-1], res[n-2])
        

        
        
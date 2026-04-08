class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate (nums):
            difference = target-n 
            for j in range(i+1,len(nums)):
                if nums [j] == difference : 
                    return [i,j]
                else : 
                    continue
            
#double loop - time complexity nxn 
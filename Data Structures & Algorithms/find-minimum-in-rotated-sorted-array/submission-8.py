class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = nums[0]
        l = 0 
        r = len(nums)-1
        while l <=r : 
            mid = (l + r)//2
            if nums [l] <= nums [mid]:
                low = min (low ,nums[l])
                l = mid +1
            else:
                low = min (low, nums[mid]) 
                r = mid -1
        return low




        
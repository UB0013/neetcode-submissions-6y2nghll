class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len (nums)-1

        while l < r :
            mid = (l+r)// 2
            if nums [l] < nums [r] and nums[l] <= nums[mid] : 
                r = mid - 1  
            elif nums[l] > nums[r] and nums[mid] < nums [r]:
                r = mid
            elif nums[l] > nums[r] and nums[mid] > nums [r]:
                l=mid +1
        return nums[l]


        
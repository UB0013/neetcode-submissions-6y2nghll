class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]: 
                # left is sorted and right side contains 
                #minimum and the pivot
                l = mid + 1
            else:
                r = mid

        return nums[l]

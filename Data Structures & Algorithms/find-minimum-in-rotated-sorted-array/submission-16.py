class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 #0 
        r = len(nums)-1 #3 
        minr = max(nums)
        while l<=r : 
            mid = (l+r)//2 
            print(mid)

            if nums[mid] <= nums[r] : 
                print (minr)
                minr = min(minr,nums[mid])
                r = mid-1  
            else : 
                l = mid +1
        

        return minr  

# nums=[4,5,6,7]

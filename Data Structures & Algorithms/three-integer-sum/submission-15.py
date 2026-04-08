class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums =  (sorted(nums))
        print(nums)
        res = []
    
        for i in range (len(nums)):

            if i > 0 and nums[i-1] == nums[i] :
                continue 
            l = i +1 
            r = len(nums) -1
            while l < r : 

                if nums [i] + nums[l] + nums [r] > 0 :
                    r = r-1
                elif nums [i] + nums[l] + nums [r] < 0 : 
                    l = l +1 
                    
                else :
                    res.append([nums[i], nums[r], nums[l]])
                    l = l +1
                    r =  r-1 
                    while nums [l] == nums[l-1] and l < r  : 
                        l = l +1 
                    
        return res 
                    

        
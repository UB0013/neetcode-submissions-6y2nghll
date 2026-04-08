class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted (nums)
        print(nums)
        res  = []
        
        for i, n in enumerate (nums) : 
            if i > 0 and n == nums [i-1] : 
                continue 
            target = -n
            l = i+1
            r = len (nums)-1  
            while l < r :  
                if nums[l] + nums[r] >  target : 
                    r = r-1 
                elif nums[l] + nums[r] < target  :
                    l = l+1
                elif nums[l] + nums[r] == target  : 
                    res.append([n, nums[l],nums[r]])
                    #print (res)
                    l = l +1 
                    r = r-1 
                    while  l-1 >= 0 and 0<=l < len (nums) and nums [l]  == nums [l-1] :
                        l = l+1 
        return res
                  


        
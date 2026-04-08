class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =[]
        nums.sort()

        for i , n in enumerate  (nums ): 

            if i > 0 and n == nums [i-1] :
                continue 
            l = i +1
            r = len(nums)-1
            while l < r : 
                sum3 = n + nums [l] + nums [r]
                if sum3 > 0 : 
                    r = r-1 
                elif sum3 < 0 : 
                    l = l+1 
                else  : 
                    result.append([n,nums[l],nums[r]])
                    l = l +1 
                    r = r-1 
                    while nums[l] == nums [l-1] and l< r: 
                        l = l +1 

        return result 

                

                
                
                



        
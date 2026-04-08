class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapp = {}
        for i , s in enumerate (nums) : 
            diff = target-s 
            if s in  mapp.keys() :
                return sorted([i, mapp[s]])
            else :
                mapp[diff] = i 
                print (mapp) 

        return [-1,-1]
        


        
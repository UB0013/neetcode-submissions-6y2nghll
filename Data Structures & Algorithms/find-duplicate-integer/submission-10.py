class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow :
                break 

        
        fast = 0 

        while True: 
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast : 
                return slow


        
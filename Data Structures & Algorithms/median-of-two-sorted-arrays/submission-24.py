class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A ,B = nums1, nums2 
        if len(nums1)>len(nums2):
            A ,B = B, A 
        total = len(nums1)+len(nums2)
        half = total//2 
        l = 0 
        r = len(A)-1
        while True :
            i = (l+r)//2
            j = half - i - 2 
            Aleft = A[i] if i >=0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >=0 else float("-inf")
            Bright = B[j+1] if (j + 1) < len(B) else float("inf")

# incorrect partition
            if Aleft > Bright  and Bright < Aleft : 
                if Aleft > Bright: 
                    r = i -1
                else : 
                    l = i +1 
            elif  total%2==0: 
                return (max(Aleft,Bleft)+ min(Aright,Bright))/2
            else : 
                return min (Bright ,Aright )

                

                
        


        
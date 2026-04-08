class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B= nums2
        if len(nums1)> len(nums2): 
            A,B = B,A

        l = 0 
        r = len(A)-1
        total = len(A)+len(B)
        half = total//2 

        while True : 
            midAL = (l+r)//2
            midBL = half - midAL -2

            Aleft = A[midAL] if midAL >= 0 else float("-inf")
            Aright  = A[midAL+1] if midAL+1 < len(A) else float("inf")
            Bleft  = B[midBL] if midBL>= 0 else  float ("-inf")
            Bright = B[midBL+1] if midBL+1 < len(B) else float ("inf")

            if Aleft <= Bright  and Bleft <= Aright : 
                if total%2 : 
                    median= min (Aright, Bright)
                    return median 
                else : 
                    median = (max (Aleft,Bleft )+ min (Aright, Bright))/2
                    return median 
            if Aleft > Bright : 
                r = midAL -1 
            else : 
                l = midAL +1





        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        m=nums1+nums2
        m.sort()
        

        n=len(m)
        mid=n//2

        if(n%2!=0):
            return m[n//2]
        else:
            return (m[mid-1]+m[mid])/2
        
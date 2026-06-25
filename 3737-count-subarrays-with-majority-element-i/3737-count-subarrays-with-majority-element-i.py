class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            
            check=0
            for j in range(i,len(nums)):
                if(nums[j]==target):
                    check+=1
                length=j-i+1
            
                if check > length//2:
                    c+=1
        
        return c
            
                

        
        
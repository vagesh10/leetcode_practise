class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        seen=set()

        
        


        for i in range(0,n):
            if i>k:
                seen.remove(nums[i-k-1])
            
            if nums[i] in seen:
                return True
            
            seen.add(nums[i])
            
        return False
        
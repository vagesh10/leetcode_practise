class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=0
        seen=set()
        ans=0
        addition=0

        for j in range(n):
            while nums[j] in seen:
                seen.remove(nums[i])
                addition-=nums[i]
                i+=1

            seen.add(nums[j])
            addition+=nums[j]
            
            if j-i+1 == k:
                ans=max(addition,ans)
                addition-=nums[i]
                seen.remove(nums[i])
                i+=1
        
        return ans
        
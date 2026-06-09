class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:


        s=sorted(nums)

        return (s[-1]-s[0])*k
        
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        s=[]
        e=[]
        l=[]
        n=len(nums)


        for i in range(n):
            if(nums[i]<pivot):
                s.append(nums[i])
        for i in range(n):
            if(nums[i]==pivot):
                e.append(nums[i])
        for j in range(n):
            if(nums[j]>pivot):
                l.append(nums[j])
            
        return s+e+l
        
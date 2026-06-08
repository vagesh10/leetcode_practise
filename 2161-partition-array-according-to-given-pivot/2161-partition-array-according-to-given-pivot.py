class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        s=[]
        e=[]
        l=[]
        n=len(nums)


        for i in range(n):
            if(nums[i]<pivot):
                s.append(nums[i])
        
            elif(nums[i]==pivot):
                e.append(nums[i])
        
            else:
                l.append(nums[i])
            
        return s+e+l
        
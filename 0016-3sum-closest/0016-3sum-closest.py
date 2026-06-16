class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:


        n=len(nums)
        nums.sort()

        closest_sum=nums[0]+nums[1]+nums[2]


        for i in range(n-2):

            left=i+1
            right=n-1
            while(left < right):
                curr=nums[i]+nums[left]+nums[right]
                
                if(abs(curr-target)<abs(closest_sum-target)):
                    closest_sum=curr
                
                if(curr < target):
                    left+=1
                elif(curr>target):
                    right-=1
                else:
                    return curr
        

        return closest_sum


       

    
        

    

        
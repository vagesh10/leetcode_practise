class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)

        left=0
        right=n-1

        maxi=0

        while(left<right):
            h=min(height[left],height[right])
            w=right-left
            Area=h*w
            maxi=max(maxi,Area)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxi

        
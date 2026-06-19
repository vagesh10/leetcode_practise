class Solution:
    def largestAltitude(self, gain: List[int]) -> int:


        n=len(gain)
        s=0
        ans=[0]*n

    

        for i in range(0,n):
            s+=gain[i]
            ans.append(s)
        print(ans)
    
        
        return max(ans)


        
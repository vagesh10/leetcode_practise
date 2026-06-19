class Solution:
    def largestAltitude(self, gain: List[int]) -> int:


        n=len(gain)
        s=0
        ans=[0]*n

    

        for i in range(n):
            s+=gain[i]
            ans.append(s)
        
        return max(ans)


        
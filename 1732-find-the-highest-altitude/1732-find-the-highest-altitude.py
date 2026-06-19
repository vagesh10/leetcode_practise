class Solution:
    def largestAltitude(self, gain: List[int]) -> int:


        n=len(gain)
        s=0
        max_height=0

    

        for i in gain:
            s+=i
            max_height=max(max_height,s)
        
        
        return max_height


        
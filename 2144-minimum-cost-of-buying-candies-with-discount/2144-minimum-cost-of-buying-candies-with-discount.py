class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        c=0
        s=sorted(cost,reverse=True)
        n=len(cost)

        
        for i in range(0,n):
            if(i%3!=2):
                c+=s[i]
        return c


        
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
       
        n=len(cost)
        c=sorted(cost,reverse=True)
        s=0
        if n==1:
            return c[0]
        if (n==2):
            return c[0]+c[1]
        
        else:
            for i in range(n):
                if(i%3!=2):
                    print(c[i])
                    s+=c[i]
        return s
            


        
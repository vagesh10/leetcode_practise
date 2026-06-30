class Solution:
    def numberOfSubstrings(self, s: str) -> int:


        n=len(s)
        left=0
        c={'a':0,'b':0,'c':0}
        res=0

        for i in range(n):

            c[s[i]]+=1

            while (c['a']>0 and c['b']>0 and c['c']>0):
                res+=len(s)-i
                c[s[left]]-=1
                left+=1
        

        return res


            
                
        




                

        return c




        
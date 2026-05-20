class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res=[]
        for i in range(len(A)):
            c=0
            for b in range(0,i+1):
                for a in range(0,i+1):
                    if(B[b]==A[a]):
                        c+=1
            
            res.append(c)
            # print(res)
        return res
                
        
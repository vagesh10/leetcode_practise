class Solution:
    def processStr(self, s: str) -> str:

        res=[]
        for i in s:
            if(i=="#"):
                res.extend(res)
            
            elif(i=="%"):
                res.reverse()
            
            elif(i=="*"):
                if res:
                    res.pop()
            else:
                res.append(i)
        

        return "".join(res)
            

        
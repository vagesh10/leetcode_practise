class Solution:
    def totalRes(self,x:int)->int:
        c=0

        s=str(x)

        for i in range(1,len(s)-1):
            if((s[i]>s[i-1] and s[i]>s[i+1]) or (s[i]<s[i-1] and s[i]<s[i+1])):
                c+=1
        
        return c
    
    def totalWaviness(self, num1: int, num2: int) -> int:

        ans=0

        for x in range(num1,num2+1):
            ans+=self.totalRes(x)
        
        return ans
        
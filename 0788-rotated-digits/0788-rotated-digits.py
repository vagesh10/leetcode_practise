class Solution:
    def rotatedDigits(self, n: int) -> int:

        
        c=0

        for i in range(1,n+1):
           isValid=True
           isChanged=False
           num=i

           while(num>0):
            digit=num%10

            if digit in [3,7,4]:
                isValid=False
                break
            if digit in [2,5,6,9]:
                isChanged=True
            num//=10
        
           if isValid and isChanged:
            c+=1



        return c

        
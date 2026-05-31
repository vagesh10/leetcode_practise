class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        if mass==1 and asteroids[0]==1 and len(asteroids)==1:
            return True

        s=sorted(asteroids)
    
        for i in s:
            if mass >= i:
                mass+=i 
               
            else:
                return False
        return True
        

       
        
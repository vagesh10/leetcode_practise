class Solution {
public:
    
    
    int reverse(int n){
        int r =0;
        while(n!=0){
            int rem=n%10;
            r=(r*10)+rem;
            n/=10;
            
            
            
        }
        return r;
    
    }
    int mirrorDistance(int n) {

       int rev= reverse(n);
        return abs(n-rev);
        
    }
};
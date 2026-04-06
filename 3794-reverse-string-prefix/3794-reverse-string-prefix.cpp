class Solution {
public:
    string reversePrefix(string s, int k) {

        int n=s.size();

        if(n==0 || n==1) return s;

       int i=0;
       int j=k-1;

       while(i<j){
          int temp=s[j];
          s[j]=s[i];
          s[i]=temp;

          i++;
          j--;
        }

        return s;


        

        
    }
};
class Solution {
public:
    string largestOddNumber(string num) {

        if(num.back()%2==1) return num;

        int n=num.length();

        int i=n-1;

        while(i>=0){
            int m=num[i];

            if(m%2!=0) return num.substr(0,i+1);
            i--;
        }

        return "";
        
    }
};
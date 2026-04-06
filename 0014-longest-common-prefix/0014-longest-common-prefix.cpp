class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        int n=strs.size();

        int k=0;
        if(n==0) return "";
        if(n==1) return strs[0];

        while(1){
            for(int i=1;i<=n-1;i++){
                if(k==strs[i].size()) return strs[0].substr(0,k);

                if(strs[i][k]!=strs[0][k]) return strs[0].substr(0,k);
            }
            k++;
        }

        return "";
        
    }
};
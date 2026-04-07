class Solution {
public:
    string reverseWords(string s) {

        stringstream word(s);

        string w;
        vector<string>words;

        while(word>>w){
            words.push_back(w);
        }

        int p=words.size();
        string ans="";

        for(int i=p-1;i>=0;i--){
            ans+=words[i]+" ";
        }

        ans.pop_back();

        return ans;
        
    }
};
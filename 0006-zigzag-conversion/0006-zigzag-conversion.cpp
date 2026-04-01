class Solution {

public:
    string convert(string s, int numRows) {

        vector<string>rows(numRows);

        if(numRows==1){
            return s;
        }
        int row=0,down=false;

        for(char c:s )
        {
            rows[row]+=c;

            if(row==0) down=true;

            else if(row==numRows-1) down=false;

            row+=down ? 1 :-1;
        }

        string result;

        for(string r : rows){
            result+=r;
        }

        return result;
        
    }
};
        
    
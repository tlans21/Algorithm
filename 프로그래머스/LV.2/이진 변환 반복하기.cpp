#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    string temp = "";
    int zerocnt = 0;
    int cnt = 0;
    while(s != "1"){
        temp = "";
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '0'){
                zerocnt++;
            }else if(s[i] == '1'){
                temp += s[i];
            }
        }
        int size = temp.size();
        
        s = "";
        while(size > 0){
            if(size % 2 == 0){
                s += "0";
                size = size / 2;
            }else if(size % 2 != 0){
                s += "1";
                size = size / 2;
            }
        }
        cnt++;
    }
    answer.push_back(cnt);
    answer.push_back(zerocnt);
    return answer;
}
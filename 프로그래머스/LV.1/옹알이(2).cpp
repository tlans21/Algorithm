#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    
    for(int i = 0; i < babbling.size(); i++){
        string s = babbling[i];
        string a = "";
        string temp = "";
        for(int j = 0; j < s.size(); j++){
            a+=s[j];
            if(a == "aya" || a == "ye" || a == "woo" || a == "ma"){
                if(temp == a){
                    break;
                }
                temp = a;
                a = "";
            }
        }
        if(a.size() == 0){
            answer++;
        }
    }
    
    
    return answer;
}
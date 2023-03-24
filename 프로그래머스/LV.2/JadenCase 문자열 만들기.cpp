#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int idx = -2;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == ' '){
            answer += s[i];
            idx = i;
        }else if(s[i] >= 'a' && s[i] <= 'z'){
            if(i == 0 || i == idx + 1){
                answer += s[i] - 32;
            }else{
                answer += s[i];
            }
        }else if(s[i] >= 'A' && s[i] <= 'Z'){
            if(i == 0 || i == idx + 1){
                answer += s[i];
            }else{
                answer += s[i] + 32;
            }                
        }else if(s[i] >= '0' && s[i] <= '9'){
            answer +=s[i];
        }
    }
    
    return answer;
}
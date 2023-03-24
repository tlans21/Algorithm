#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    if(s.size() % 2 != 0){
        //홀수인 경우
        answer +=s.substr(s.size() / 2, 1);
    }else{
        answer +=s.substr(((s.size()-1) / 2), 2);
    }
    
    return answer;
}
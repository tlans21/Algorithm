#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    
    int temp = 0;
    int temp1 = 0;
    int first_index = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[first_index] == s[i]){
            temp++;
        }else if(s[first_index] != s[i]){
            temp1++;
        }
        if(temp == temp1){
            answer++;
            first_index = i+1;
        }
        if(i == s.size() -1 && temp != temp1)
        {
            answer++;
        }
    }
    return answer;
}
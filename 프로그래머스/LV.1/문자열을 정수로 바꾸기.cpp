#include <string>
#include <vector>
#include <string>
using namespace std;
int multi(char s, int size){
    if(size == 0){
        return (int)s;
    }
    int k = (int)s;
    while(size){
        k = k * 10;
        size--;
    }
    return k;
}

int solution(string s) {
    int answer = 0;
    int size = s.size() - 1;
    for(int i = 0; i < s.size(); i++){
        if(s[0] == '+'){
            size = s.size() - 2;
            continue;
        }else if(s[0] == '-'){
            size = s.size() - 2;
            continue;
        }
        answer += multi(s[i], size);
        size--;
    }
    
    return answer;
}
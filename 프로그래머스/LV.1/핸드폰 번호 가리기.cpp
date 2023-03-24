#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = "";
    // 맨 마지막 인덱스 size -1 부터 이므로 size - 1, size - 2, size - 3, size - 4다
    for(int i = 0; i < phone_number.size(); i++){
        if( i >= phone_number.size() - 4 ){
            answer += phone_number[i];
        }else{
            answer += "*";
        }
    }
    return answer;
}
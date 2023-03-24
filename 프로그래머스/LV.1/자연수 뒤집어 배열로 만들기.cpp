#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    // idea 일의 자리를 0번째 인덱스에, 십의 자리를 1번째 인덱스에.. 반복
    
    while(1){
        long long part = n % 10;
        n = n / 10;
        
        answer.push_back((int)part);
        if(n == 0){
            break;
        }
    }
    return answer;
}
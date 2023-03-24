#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    if(a > b){
        int temp = a; // a를 임의 적으로 저장
        a = b; // b값을 a로 옮김
        b = temp; // 저장해둔 a값을 b로 옮김
    }
    
    for(long long i = a; i <= b; i++){
        answer += i;
    }
    return answer;
}
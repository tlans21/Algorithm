#include <iostream>

using namespace std;
int solution(int N)
{
    int answer = 0;
    while(1){
        answer += N % 10; // 나머지 값를 통하여 일의 자리를 추출
        N = N / 10; //일의 자리를 추출하였으므로 새로운 일의 자리를 앞으로 당기기위해 10으로 나눈다.
        if(N == 0){
            break;
        }
    }
    return answer;
}
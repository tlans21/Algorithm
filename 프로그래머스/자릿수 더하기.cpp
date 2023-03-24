#include <iostream>

using namespace std;
int solution(int N)
{
    int answer = 0;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;
    int checkLoc = 1;
    while(1){
        if((N / checkLoc) == 0){
            break; // while문을 빠져나왔을 때, checkLoc로 N이 어떤 자리수 인지 알 수 있다.
        }
        checkLoc *= 10;
    }
    checkLoc = checkLoc / 10;
    
    int sum = 0;
    int K = N;
    while(1){
        int part = K / checkLoc;
        K = K - (part * checkLoc);
        sum += part;
        checkLoc = checkLoc / 10;
        if(checkLoc == 0){
            break;
        }
    }
    answer = sum;
    return answer;
}
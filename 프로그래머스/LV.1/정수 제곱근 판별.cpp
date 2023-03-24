#include <string>
#include <vector>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    long long storge = 0;
    bool flag = false;
    
    for(long long i = 1; i <= n; i++){
        if(i * i == n){
            storge = i;
            flag = true;
            break;
        }else if(i * i > n){
            break;
        }
    }

    
    if(flag){
        answer = (storge + 1) * (storge + 1);
    }else{
        answer = -1;
    }
    
    return answer;
}
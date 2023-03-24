#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int sum = 0;
    int tempX = x;
    while(x){
        int k = x % 10;
        x = x / 10;
        sum += k;
        if(x == 0){
            break;
        }
    }
    if(tempX % sum != 0){
        answer = false;
    }
    return answer;
}
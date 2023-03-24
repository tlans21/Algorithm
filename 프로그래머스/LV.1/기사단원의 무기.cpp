#include <string>
#include <vector>

using namespace std;

int prime_number(int k){
    int cnt = 0;
    if(k < 1){
        return 0;
    }
    for(int i = 1; i * i<= k; i++){
        if(k % i == 0){
            cnt++;
            if((k / i) != i){
                cnt++;
            }
        }
    }
    return cnt;
}


int solution(int number, int limit, int power) {
    int answer = 0;
    vector<int> knights;
    int cnt = 0;
    for(int i = 0; i <= number; i++){
        if(i == 0){
            knights.push_back(0);
            continue;
        }
        cnt = prime_number(i);
        knights.push_back(cnt);
    }
    
    for(int i = 1; i <= number; i++){
        if(knights[i] > limit){
            knights[i] = power;
        }
    }
    
    for(int i = 1; i <= number; i++){
        answer += knights[i];
    }
    return answer;
}
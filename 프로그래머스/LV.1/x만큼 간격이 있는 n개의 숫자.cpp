#include <string>
#include <vector>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    int k = x;
    for(int i = 0; i < n; i++){
        answer.push_back(k);// 첫번째는 그대로. 
        k += x; // x+=x 를 해주면 x값이 변하면서 더하기 때문에 안됨.
    }
    
    return answer;
}
#include <string>
#include <vector>
#include<algorithm>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;

    //인용되는 논문의 중간 값을 찾아야함.
    sort(citations.begin(), citations.end(), greater<>());

    
    if(!citations[0]){
        return 0;
    }
    for(int i = 0; i <= citations.size(); i++){
        if(citations[i] >= i+1){
            answer++;
        }else{
            break;
        }
    }
    return answer;
}
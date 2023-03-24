#include <string>
#include <vector>

using namespace std;
int cnt = 0;
int combination(int depth, int index, int answer1, vector<int> number){
    if(depth == 3){
        if(answer1 == 0){
            cnt++;
        }
    }
    
    for(int i = index; i < number.size(); i++){
        combination(depth + 1, i + 1, answer1 + number[i], number);
    }
    return 0;
}

int solution(vector<int> number) {
    int answer = 0;
    combination(0, 0, 0, number);
    answer = cnt;
    return answer;
}
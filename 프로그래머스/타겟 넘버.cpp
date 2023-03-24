#include <string>
#include <vector>

using namespace std;
int cnt = 0;
int visit[51];
int dfs1(vector<int> numbers,int s,int depth, int target){
    if(numbers.size() == depth){
        if(target == s){
            cnt++;
        }
        return 0;
    }

    for(int i = 0; i < numbers.size(); i++){
        if(visit[i] == 1){
            continue;
        }else{
            visit[i] = 1;
            dfs1(numbers, s + numbers[i], depth+1, target);
            visit[i] = 0;

            visit[i] = 1;
            dfs1(numbers, s - numbers[i], depth+1, target);
            visit[i] = 0;
        }
    }
    return 0;
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    dfs1(numbers, 0, 0, target);
    answer = cnt;
    return answer;
}

// 오류 코드 위는 순서가 바뀌는 경우도 계산해 준 것이다.
//ex) 1 + 2 +  3 +  4을 3 + 2+ 1 + 4 로 바꿔서 계산해준것도 포함.




int dfs(vector<int> numbers, int s, int target, int depth){
    if(numbers.size() == 0){
        return 0;
    }

    if(numbers.size() == depth){
        if(s == target){
            cnt++;
        }
        return;
    }

    dfs(numbers, s+numbers[depth], target, depth+1);
    dfs(numbers, s-numbers[depth], target, depth+1);

    return cnt;
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    answer = dfs(numbers, 0, target, 0);
    return answer;
}
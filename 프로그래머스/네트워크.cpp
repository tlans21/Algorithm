#include <string>
#include <vector>

using namespace std;
int visit[201];

int dfs(int start, vector<vector<int>> computers){
    
    visit[start] = 1;
    
    for(int i = 0; i < computers[start].size(); i++){
        int next = computers[start][i];
        if(start == i){
            continue;
        }
        if(next == 1 && !visit[i]){
            dfs(i, computers);
        }
    }
    return 0;
}
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    //dfs를 해서 방문처리를 하게되면 안된 곳을 알 수있다.

    for(int i = 0; i < computers.size(); i++){
        if(visit[i] != 1){
            dfs(i, computers);
            answer++;
        }
    }


    return answer;
}
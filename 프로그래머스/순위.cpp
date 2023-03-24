#include <string>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;

int maxdepth = 0;
int visit[101];
int loseCnt[101];
int winCnt[101];

priority_queue<int, greater<int>> pq;
int dfs(int start, vector<vector<int>>results){
    int count = 0;
    visit[start] = 1;
    
    for(int i = 0; i < results.size(); i++){
        int next = results[i][1];
        if(!visit[next] && (start == results[i][0])){
            count = count + dfs(next, results) + 1;
        }
    }
    return count;
}
int dfs2(int start, vector<vector<int>>results){
    int count = 0;
    visit[start] = 1;
    
    for(int i = 0; i < results.size(); i++){
        int next = results[i][0];
        if(!visit[next] &&(start == results[i][1])){
            count = count + dfs2(next, results) + 1;
        }
    }
    return count;
}
int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    
    //DFS를 통해 이긴 경우를 구하기
    
    
    //이긴 횟수와 진 횟수를 더했을 때, n-1이라면 해당하는 등수를 알 수 있다.
    for(int i = 1; i <= n; i++){
        int count1 = dfs(i, results);
        memset(visit, 0, sizeof(visit));
        int count2 = dfs2(i, results);
        memset(visit, 0, sizeof(visit));
        if((count1 + count2)== n-1){
            answer++;
        }
    }
    return answer;
}
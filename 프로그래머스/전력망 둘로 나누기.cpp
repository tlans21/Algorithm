#include <string>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int visited[200];
vector<int> v[102];
int cnt = 0;


int dfs(int cur, int st, int end){
    cnt++; // 개수 카운트. 
    visited[cur] = 1;
    for(int i = 0; i < v[cur].size(); i++){
        int next = v[cur][i];
        if((cur == st && next == end )|| (next == st && cur == end)){
            continue;
        }else{
            if(!visited[next]){
                dfs(next, st, end);
            }
        }
    }
    return cnt;
}


int solution(int n, vector<vector<int>> wires) {
    int answer = 987654321;
    
    
    for(int i = 0; i < wires.size(); i++){
        v[wires[i][0]].push_back(wires[i][1]);
        v[wires[i][1]].push_back(wires[i][0]);
    } // 간선 연결

    for(int i = 0; i < wires.size(); i++){
        int st = wires[i][0];
        int end = wires[i][1];
        vector<int> storge;
        fill(visited, visited+200, 0);

        for(int j = 1; j <= wires.size(); j++){
            if(visited[j] == 0){
                int temp = dfs(j, st, end);
                cnt = 0;
                storge.push_back(temp);
            }
        }
        answer = min(answer, abs(storge[0]-storge[1]));
    }
    
    return answer;
}
#include<iostream>
#include <string>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;


vector<int> adj[20001];

int visit[20001];

int maxCnt = -1;
int temp = 0;
int flag = 0;

vector<int> storge(20001, 0);
int bfs(int start, int depth){
    queue<pair<int,int>> q;
    visit[start] = 1;
    q.push({start, 0});
    while(!q.empty()){
        int cur = q.front().first;
        int cnt = q.front().second;
        q.pop();
        //최대 깊이 구하기 
        
        // 최대 길이를 갖는 노드 카운트

        
        for(int i = 0; i < adj[cur].size(); i++){
            int next = adj[cur][i];
            int nextCnt = cnt + 1;
            if(!visit[next]){
                visit[next] = 1;
                q.push({next, nextCnt});
                maxCnt = max(maxCnt, nextCnt);
                if(flag == 1){
                    if(maxCnt == nextCnt){
                        temp++;
                    }
                }
            }
        }
    }
    return 0;
}
int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    
    for(int i = 0; i < edge.size(); i++){
        int from = edge[i][0];
        int to = edge[i][1];
        adj[from].push_back(to);
        adj[to].push_back(from);
    }
    
    bfs(1, 0);
    flag = 1;
    memset(visit, 0, sizeof(visit));
    bfs(1, 0);
    answer = temp;
    return answer;
}


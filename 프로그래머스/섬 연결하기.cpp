#include <string>
#include <vector>
#include <queue>
#include <cstring>
#define INF 99999

using namespace std;
int dist[101];
bool visit[101];

vector<pair<int,int>> adj[101];

void dijkstra(int start){
    priority_queue<pair<int,int>> pq;
    dist[start] = 0;
    pq.push({0, start});
    
    while(!pq.empty()){
        int Cost = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        if(visit[cur]){
            continue;
        }
        visit[cur] = true;
        for(int i = 0; i < adj[cur].size(); i++){
            int next = adj[cur][i].first;
            int nCost = adj[cur][i].second;
            if(dist[next] > nCost && !visit[next]){
                dist[next] = nCost; // 다음 거리 값 갱신
                pq.push({-nCost, next});
            }
        }
    }
}
int solution(int n, vector<vector<int>> costs) {
    int answer = 9876543211;
    
    int E = costs.size();
    for(int i = 0; i < costs.size(); i++){
        int from = costs[i][0];
        int to = costs[i][1];
        int cost = costs[i][2];
        
        adj[from].push_back({to, cost});
        adj[to].push_back({from, cost});
    }
    for(int i = 0; i < n; i++){
        int temp = 0;
        for(int j = 0; j < n; j++){
            dist[j] = INF;
        }
        dijkstra(i);
        
        for(int s = 0; s < n; s++){
            if(visit[s]){
                temp += dist[s];
            }
        }
        
        answer = min(temp, answer);
        memset(visit, false, sizeof(visit));
    }
    return answer;
}
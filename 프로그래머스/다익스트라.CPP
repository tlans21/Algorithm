#include<iostream>
#include <queue>

using namespace std;

int dist[10001];
int visit[10001];
vector<pair<int,int>> graph[100001];
void dijkstra(int start){
    priority_queue<pair<int,int>> pq;
    dist[start] = 0;
    visit[start] = 1;
    pq.push({0, start});
    while(!pq.empty()){
        int dist = -pq.top().first;
        int now = pq.top().second;
        for(int i = 0; i < graph[now].size(); i++){
            int next = graph[now][i].first;
            int ncost = graph[now][i].second;
            if(!visit[next]){
                visit[next] = 1;
                pq.push({-ncost, next});
            }

        }
    }
}
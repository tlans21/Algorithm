#include<iostream>
#include<vector>
#include<queue>
#include<string.h>

#define INF 100000000
using namespace std;
int N;
int M;
int dist[1001];
vector<pair<int, int>> a[10001];

int dijkstra(int start, int end){
    priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int>>>pq;
    for(int i = 0; i <= N; i++){
        dist[i] = INF;
    }
    dist[start] = 0;
    pq.push({0, start});
    while(!pq.empty()){
        int cur = pq.top().second;
        int cost = pq.top().first;
        pq.pop();
        if(dist[cur] < cost){
            continue;
        }
        for(int i = 0; i <a[cur].size(); i++){
            int next = a[cur][i].first;
            int ncost = a[cur][i].second;
            if(dist[next] > ncost + cost){
                dist[next] = ncost + cost;
                pq.push({dist[next], next});
            }
        }
    }
    return dist[end];
}
int main(){
    int X;
    int u;
    int v;
    int w;
    int ans = 0;
    int temp;
    cin>>N>>M>>X;
    for(int i = 1; i <= M; i++){
        cin>>u>>v>>w;
        a[u].push_back({v, w});
    }

    for(int i = 1; i<=N; i++){
       temp = dijkstra(i, X) + dijkstra(X, i);
       ans = max(ans, temp);
    }
    cout<<ans;
 
    return 0;
}
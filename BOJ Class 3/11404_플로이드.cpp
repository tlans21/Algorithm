#include<iostream>
#include<queue>
#include<vector>
#define INF 1000000

using namespace std;

int N;
int M;

int dist[101]; // 값을 저장하는 배열.
vector<pair<int, int>> a[100001]; // 버스.

void dijkstra(int start){
    for(int i = 0; i <= N; i++){
        dist[i] = INF;
    }
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push({0, start});
    while(!pq.empty()){
        int cur = pq.top().second;
        int cost = pq.top().first;
        pq.pop();
        for(int i = 0; i < a[cur].size(); i++){
            int next = a[cur][i].first;
            int distance = a[cur][i].second + cost;
            if(dist[next] > distance){
                dist[next] = distance;
                pq.push({dist[next], next});
            }
        }
    }
}

int main(){

    cin>>N>>M;

    for(int i = 0; i < M; i++){
        int x;
        int y;
        int z;
        cin>>x>>y>>z;
        a[x].push_back({y, z});
    }

    for(int i = 1; i <= N; i++){
        dijkstra(i);
        for(int j = 1; j <= N; j++){
            
                cout<<dist[j]<<" ";
            
        }
        cout<<'\n';
    }
}
#include<iostream>
#include<vector>
#include<queue>
#define INF 100000000

using namespace std;
vector<pair<int, int>> a[801];

int dist[801];
int N;
int E;
void dijkstra(int start){
      for(int i = 0; i <= N; i++){
        dist[i] = INF;
    }
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push(make_pair(0, start));
    while(!pq.empty()){
        int cur = pq.top().second;
        int cost = pq.top().first;
        pq.pop();
        if(dist[cur] < cost){
            continue;
        }
        for(int i = 0; i < a[cur].size(); i++){
            int next = a[cur][i].first;
            int ncost = a[cur][i].second;
            if(dist[next] > ncost + cost){
                dist[next] = ncost + cost;
                pq.push({dist[next], next});
            }
        }
    }
}

int main(){
    cin >> N >> E;
    int x;
    int y;
    int z;
    int v1;
    int v2;
    int ans = INF;

  

    for(int i = 0; i < E; i++){
        cin>>x>>y>>z;
        a[x].push_back({y, z});
        a[y].push_back({x, z});
    }
    cin>>v1>>v2;

    dijkstra(1);
    int first_tov1 = dist[v1];
    int first_tov2 = dist[v2];

    dijkstra(v1);
    int v1tov2 = dist[v2];
    int v1toN = dist[N];
    
    dijkstra(v2);
    int v2toN = dist[N];

    ans = min(ans, first_tov1 + v1tov2 + v2toN);
    ans = min(ans, first_tov2 + v1tov2 + v1toN);

    if(v1tov2 == INF || ans == INF){
        cout<<-1;
    }else{
        cout<<ans;
    }



    return 0;
}
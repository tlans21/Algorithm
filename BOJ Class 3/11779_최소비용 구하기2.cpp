#include<iostream>
#include<vector>
#include<queue>

#define INF 100000000

using namespace std;

int dist[1001];
int N;
int M;
vector<pair<int, int>> a[100001];
int location[100001];

void dijkstra(int start){
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    for(int i = 0; i <= N; i++){
        dist[i] = INF;
    }
    dist[start] = 0;
    pq.push({0, start});
    while(!pq.empty()){
        int cost = pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        if(dist[cur] < cost){
            continue;
        }

        for(int i = 0; i < a[cur].size(); i++){
            int ncost = a[cur][i].second + cost;
            int next = a[cur][i].first;
            if(dist[next] > ncost){
                dist[next] = ncost;
                location[next] = cur;
                pq.push({dist[next], next});
            }
        }
    }    
}
int main(){
    int start;
    int end;

    cin>>N;
    cin>>M;
    for(int i = 1; i <= M; i++){
        int x;
        int y;
        int z;
        cin>>x>>y>>z;
        a[x].push_back({y, z});   
    }

    cin>>start>>end;
    dijkstra(start);
    cout<<dist[end]<<'\n';

    int idx = end;

    vector<int> s;
    while(idx){
        s.push_back(idx);
        idx = location[idx];
    }

    cout<< s.size() <<'\n';
    for(int i = s.size() - 1; i >= 0; i--){
        cout<<s[i]<<" ";
    }
}
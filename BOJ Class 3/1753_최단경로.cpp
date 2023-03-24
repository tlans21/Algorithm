#include<iostream>
#include<queue>
#include<vector>
#define INF 10000000
using namespace std;

vector<pair<int, int>> a[300001];
priority_queue<pair<int,int>>pq;
int d[20001];



int main(){
    int start;
    int V;
    int E;
    int u;
    int v;
    int w;

    cin>>V>>E;
    cin>>start;

    for(int i = 1; i <= V; i++){
        d[i] = INF;
    }

    for(int i = 0; i < E; i++){
        cin>>u>>v>>w;
        a[u].push_back({v, w});
    }

     d[start] = 0;
    pq.push({0, start});
    while(!pq.empty()){
        int cur = pq.top().second;
        int cost = -pq.top().first;
   
        pq.pop();
        for(int i = 0; i < a[cur].size(); i++){
            int next = a[cur][i].first;
            int ncost = a[cur][i].second;
            if(ncost + cost < d[next]){
                d[next] = ncost + cost;
                pq.push({-d[next], next});
            }
        }
    }

    for(int i = 1; i <= V; i++){
        if(d[i] != 10000000){
        cout<<d[i]<<'\n';
        }
        else{
            cout<<"INF"<<'\n';
        }
    }

return 0;
}
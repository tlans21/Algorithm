#include<iostream>
#include<queue>
#include<vector>

#define INF 100000000;

using namespace std;

vector<pair<int, int>> a[1001];
priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int>>>pq;
int d[1001];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int N;
    int M;
    int start;
    int end;
    cin>>N>>M;
    for(int i = 1; i <= N; i++){
        d[i] = INF;
    }
    for(int i = 1; i <= M; i++){
        int x, y, z;
        cin>>x>>y>>z;
        a[x].push_back({y, z});
    }
    cin>>start>>end;
   
    pq.push(make_pair(0, start));
    d[start] = 0;
    while(!pq.empty()){
        int cost = pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        if(d[cur] < cost){
            continue;
        }
        for(int i = 0; i < a[cur].size(); i++){
            int Next = a[cur][i].first;
            int ncost = a[cur][i].second;
            if(d[Next] > cost + ncost){
                d[Next] = cost + ncost;
                pq.push(make_pair(d[Next], Next));
            }
        }
    }
    cout<<d[end]<<endl;
    return 0;
}


#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

#define INF 987654321
using namespace std;

vector<pair<int, int>> v[101];
int dist[101];
int item[101];

int n;
int m;
int r;



void dijkstra(int start){
    for(int i = 0; i <= n; i++){
        dist[i] = INF;
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push({0, start});
    
    while(!pq.empty()){
        int cost = pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        
        for(int i = 0; i < v[cur].size(); i++){
            int ncost = cost + v[cur][i].second;
            int next = v[cur][i].first;
            if(ncost > m){
                continue;
            }
            if(dist[next] > ncost){
                dist[next] = ncost; 
                pq.push({dist[next], next});
            }
        }
    }
}


int main(){
    int a;
    int b;
    int L;
    int sum;
    int solution = 0;
    cin>>n>>m>>r;
    for(int i = 1; i <= n; i++){
        cin>>item[i];
    }
    for(int i = 1; i <= r; i++){
        cin>>a>>b>>L;
        v[a].push_back({b, L});
        v[b].push_back({a, L});
    }
    for(int i = 1; i <= n; i++){
    dijkstra(i);
    sum = 0;
    for(int j = 1; j <= n; j++){
        if(dist[j] <= m){
            sum +=item[j];
        }   
    }
    solution = max(solution, sum);
}

cout<<solution;
return 0;
}



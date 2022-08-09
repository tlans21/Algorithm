#include<iostream>
#include<vector>
#include<string.h>

using namespace std;

vector<pair<int, int>> a[100001];

int visited[100001];
int ans = 0;
int endpoint;

void dfs(int start, int length){

    if(visited[start] == true){
        return;
    }

    if(ans < length){
        ans = length;
        endpoint = start;
    }

    visited[start] = true;

    for(int i = 0; i < a[start].size(); i++){
        int next = a[start][i].first;
        int cost = a[start][i].second;
        if(!visited[next]){
            dfs(next, cost + length);
        }
    }
}

int main(){
    int V;
    int x;
    int y;
    int w;
    cin>> V;
    for(int i = 0; i < V; i++){
        cin >> x;
        while(1){
            cin>>y;
            if(y == -1){
                break;
            }
            cin>>w;
            a[x].push_back({y, w});
            a[y].push_back({x, w});
            }
    }
    dfs(1, 0);
    ans = 0;
    memset(visited, false, sizeof(visited));
    dfs(endpoint, 0);

    cout<<ans;
    
    return 0;

}





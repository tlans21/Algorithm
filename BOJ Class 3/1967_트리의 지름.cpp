#include<iostream>
#include<vector>
#include<string.h>

#define MAX 10001
using namespace std;

vector<pair<int, int>>v[MAX];
bool visited[10001] = {false};
int ans = 0;
int endpoint = 0;

void dfs(int num, int length){
    if(visited[num]){
        return;
    }

    visited[num] = true;

    if(ans < length){
        ans = length;
        endpoint = num;
    }

    for(int i = 0; i < v[num].size(); i++){
        int next = v[num][i].first;
        int cost = v[num][i].second;
        if(!visited[next]){
            dfs(next, cost+length);
        }
    }
}

int main(){

    int N;
    int a;
    int b;
    int c;
    cin>>N;

    for(int i = 0; i < N-1; i++){
        cin>>a>>b>>c;
        v[a].push_back({b, c});
        v[b].push_back({a, c});
    }

    dfs(1, 0);
    ans = 0;
    memset(visited, false, sizeof(visited));
    dfs(endpoint, 0);

    cout<<ans<<endl;

    

    return 0;
}
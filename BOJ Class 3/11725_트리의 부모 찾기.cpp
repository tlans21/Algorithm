#include<iostream>
#include<vector>
#define MAX 100001
using namespace std;

vector<int> v[MAX]; // 간선
bool visited[MAX];
int parents[MAX];


void dfs(int num){

    visited[num] = true;

    for(int i = 0; i < v[num].size(); i++){
        int y = v[num][i];
        if(!visited[y]){
            parents[y] = num;
            dfs(y);
        }
    }
}

int main(){
    int N;
    int a;
    int b;
    cin>>N;
    for(int i = 0; i < N - 1; i++){
        cin>>a>>b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    dfs(1);
    for(int i = 2; i <= N; i++){
        cout<<parents[i]<<'\n';
    }

    return 0;
}
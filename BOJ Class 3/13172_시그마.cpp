#include<iostream>
#include<queue>
#include<algorithm>

using namespace std;
int N;
int M;
int visited[501][501];
int map[501][501];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int cnt;
void dfs(int x, int y){
    visited[x][y] = 1;
    cnt++;
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx < 0 || nx >= N || ny < 0 || ny >= M){
            continue;
        }

        if(!visited[nx][ny] && map[nx][ny] == 1){
            dfs(nx, ny);
        }
    }
}

int main(){
    
    cin>>N>>M;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin>>map[i][j];
        }
    }
    int cnt1;
    int res = 0;
    int picture = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            if(map[i][j] == 1 && !visited[i][j]){
                picture++;
                cnt = 0;
                dfs(i, j);
                res = max(cnt, res);
            }
        }
    }

    cout<<picture<<'\n';
    cout<<res<<endl;
}
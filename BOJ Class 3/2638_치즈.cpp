#include<iostream>
#include<queue>

using namespace std;
int N;
int M;
bool visited[101][101];
int map[101][101];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int cnt = 0;

queue<pair<int, int>> q;

bool checking(){
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(map[i][j]){
                return false;
            }
        }
    }
    return true;
}

void BFS(){
    cnt++;
    int nextvisted[N][M];
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            nextvisted[i][j] = map[i][j];
            visited[i][j] = false;
        }
    }
    q.push(make_pair(0, 0));
    visited[0][0] = true;
   
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >= N || nx < 0 || ny >= M || ny < 0){
            continue;
        }

        if(visited[nx][ny]){
            continue;
        }
        
        if(map[nx][ny]){
            map[nx][ny]++;
        }
        if(!map[nx][ny]){
            visited[nx][ny] = true;
            q.push(make_pair(nx, ny));
        }
        }
    }

    for(int i = 0; i <N; i++){
        for(int j = 0; j < M; j++){
            if(map[i][j] - 1>=2){
            nextvisted[i][j] = 0;
            }
            map[i][j] = nextvisted[i][j];
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
    while(!checking()){
        BFS();
    }
    cout<<cnt;
}

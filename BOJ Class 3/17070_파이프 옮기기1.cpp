#include<iostream>

using namespace std;

int N;
int map[18][18];
int cnt;

int dx[3] = {0, 1, 1}; // 가로, 세로, 대각선
int dy[3] = {1, 0, 1};
void dfs(int x, int y, int kind){

    if(x == N && y == N){
        cnt++;
        return;
    }

    for(int i = 0; i < 3; i++){
        if((i == 0 && kind == 1) || (i == 1 && kind == 0)){
            continue;
        }

        int ny = y + dy[i];
        int nx = x + dx[i];
        if(ny>N || nx>N || map[nx][ny] == 1){
            continue;
        }

        if(i == 2 && (map[x+1][y] == 1 || map[x][y+1] == 1)){
            continue;
        }
        dfs(nx, ny, i);
    }
}


int main(){
    cin>>N;
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <=N; j++){
            cin>>map[i][j];
        }
    }

    dfs(1, 2, 0);
    cout<<cnt;
    return 0;
}
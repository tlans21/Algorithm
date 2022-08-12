#include<iostream>

using namespace std;
int M; // 세로 크기
int N; // 가로 크기
int dx[4] = {-1, 1, 0, 0}; //왼쪽 오른쪽 아래 위에 대한 인덱스
int dy[4] = {0, 0, 1, -1}; 
int DP[501][501] = {0,};
int height[501][501] = {0,};
int cnt = 0;
int dfs(int x, int  y){
    //도착했으면 경로 개수파악
    if(x == M && y == N){
        return 1;
    }
    if(DP[x][y] != -1){
        return DP[x][y];
    }

    DP[x][y] = 0;

    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx <= 0 || nx > M || ny <= 0 || ny > N){
            continue;
        }
        if(height[x][y] > height[nx][ny]){
            DP[x][y] = DP[x][y] + dfs(nx, ny);
        }
    }
    return DP[x][y];
}

int main(){
    cin>>M>>N;

    for(int i = 1; i <= M; i++){
        for(int j = 1; j <= N; j++){
            cin>>height[i][j];
            DP[i][j] = -1; 
        }
    }

    int answer = dfs(1,1);

    cout<<answer;
    return 0;
}
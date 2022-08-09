#include<iostream>
#include<queue>

using namespace std;
typedef struct {
    int x;
    int y;
    int wall;
}a;

int N;
int M;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0 ,-1, 1};
int map[1001][1001];
int sum[1001][1001];
bool visited[1001][1001][2];
queue<a> q;

int bfs(int x, int y, int z){
    visited[x][y][0] = true;
    q.push({x, y, z});
    while(!q.empty()){


        for(int i = 0; i < 4; i++){
        int nx = q.front().x + dx[i] ;
        int ny = q.front().y + dy[i];
        int wall = q.front().wall;
        q.pop();

       if (nx > 0 && ny > 0 && nx <= N && ny <= M) {
                if (map[nx][ny] == 1 && wall == 0 && !visited[nx][ny][wall + 1]) {
                    visited[nx][ny][wall + 1] = true;
                    sum[nx][ny] = sum[x][y] + 1;
                    q.push({ nx,ny,wall + 1 });
                }
               
                if (map[nx][ny] != 0 && !visited[nx][ny][wall]) {
                    visited[nx][ny][wall] = true;
                    sum[nx][ny] = sum[x][y] + 1;
                    q.push({ nx,ny,wall });
                }
                if (nx == N && ny == M) {
                    return sum[nx][ny];
                }
            }
        }
    }
    return -1;
}
int main(){

    cin >> N >> M;    
    for(int i = 1; i <= N; i++){
        string temp;
        cin >> temp;
        for(int j = 1; j <= M; j++){
            map[i][j] = temp[j-1] - '0';
        }
    }
	cout << bfs(1, 1, 0);
	return 0;
}

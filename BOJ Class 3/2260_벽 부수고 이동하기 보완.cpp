#include<iostream>
#include<queue>

using namespace std;

int map[1001][1001];
int visited[1001][1001][2];
int result[1001][1001];
int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, -1, 1};
int N;
int M;

int bfs(){
  queue<pair<pair<int, int>, pair<int, int>>> q;
  q.push(make_pair(make_pair(0, 0), make_pair(0, 1)));
  visited[0][0][0] = 1;
  while(!q.empty()){
      int x = q.front().first.first;
      int y = q.front().first.second;
      int wall = q.front().second.first;
      int cnt = q.front().second.second;
      q.pop();

      if(x == N-1 && y == M-1){
          return cnt;
      }
      for(int i = 0; i < 4; i++){
          int nx = x + dx[i];
          int ny = y + dy[i];

          if(nx>=0 && nx < N && ny>=0 && ny<M){
              //벽이 있고 아직 벽을 안부순 상태에서, 방문을 안한경우
              if(map[nx][ny] == 1 && wall == 0 && visited[nx][ny][wall+1] == 0){
                  visited[nx][ny][wall+1] == 1;
                  q.push((make_pair(make_pair(nx, ny), make_pair(wall+1, cnt + 1))));
              }
              //벽을 부쉈던 경험이 있거나 안 부순 경험이 유무 상관없이 방문을 안한 경우
              if(map[nx][ny] == 0 && visited[nx][ny][wall] == 0){
                  visited[nx][ny][wall] = 1;
                  q.push((make_pair(make_pair(nx, ny), make_pair(wall, cnt + 1))));                
              }
          }
        }
    }
    return -1;
}

int main() {
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		string temp;
        cin >> temp;
		for (int j = 0; j < M; j++){
        map[i][j] = temp[j] - '0';
        }
	}
	cout << bfs();
	return 0;
}
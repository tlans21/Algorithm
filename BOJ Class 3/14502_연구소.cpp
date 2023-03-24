#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

int N;
int M;
int safetyzone = 0;
vector<pair<int, int>> store;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int map[8][8];
int mapcopy[8][8];

int BFS(){
    queue<pair<int, int>> q;
    for(int i = 0; i < store.size(); i++){
        q.push(make_pair(store[i].first, store[i].second));
    }
    while(!q.empty()){
        int x = q.front().first; 
        int y = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= N || ny < 0 || ny >= M){
                continue;
            }

            if(mapcopy[nx][ny] == 0){
                mapcopy[nx][ny] = 2;
                q.push(make_pair(nx, ny));
            }
        }
    }
    int size = 0;
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            if(mapcopy[i][j] == 0){
                size++;
            }
        }
    }
    safetyzone = max(safetyzone, size);
    return safetyzone;
}

int wall(int cnt){
    if(cnt == 3){
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                mapcopy[i][j] = map[i][j];
                }
        }
        return BFS();;
    }
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            if(map[i][j] == 0){
                map[i][j] = 1;
                wall(cnt + 1);  // 백트레킹을 이용한 순열 방식으로 3개를 정한다.
                map[i][j] = 0;
            }
        }
    }
}
int main(){
    cin >> N >> M;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin>>map[i][j];
            if(map[i][j] == 2){
                store.push_back(make_pair(i, j));
            }
        }
    }
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            if(map[i][j] == 0){
                map[i][j] = 1;
                wall(1);
                map[i][j] = 0;
            }
        }
    }

    cout << safetyzone;
    return 0;
}
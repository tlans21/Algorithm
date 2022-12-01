#include<iostream>
#include<queue>
#include<vector>
#include<string.h>

using namespace std;
queue<pair<pair<int, int>, int>> q;

int N;
int eatDistance = 10100000;
int map[21][21];
int visited[21][21] = {0};
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int bx;
int by;
int eat = 0;
int sz = 2;
int sum = 0;
int fish = 0;
void bfs(int x, int y, int time){
    q.push(make_pair(make_pair(x, y), time));
     // 방문했다는 뜻
    
    while(!q.empty()){
        int curX = q.front().first.first;
        int curY = q.front().first.second;
        int count = q.front().second; // 여태까지 아기상어가 행동한 시간
        q.pop();
        for(int i = 0; i < 4; i++){
            int nx = dx[i] + curX;
            int ny = dy[i] + curY;
            if(nx < 0 || nx >= N || ny < 0 || ny >= N || visited[ny][nx] || map[ny][nx] > sz){
                continue;
            }
            if(map[ny][nx] > sz && map[ny][nx] != 9){
                continue;
            }else if(map[ny][nx] == sz || map[ny][nx] == 0 ){
                visited[ny][nx] = count + 1;
                q.push({{nx, ny}, count+1});  // 지나가기만한다.       
            }else if(map[ny][nx] < sz && map[ny][nx] != 0){
                fish++;
                if(map[ny][nx] > 0){
                    map[ny][nx] = 0;
                }
                if(eatDistance > count + 1){
                    eatDistance = count + 1; //bfs 최단거리에 있는 물고기 거리
                }
                visited[ny][nx] = count + 1;
                
                q.push({{nx, ny},count+1});
            }
        }
        
    }     
}
int main(){
    cin>>N;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin>>map[i][j];
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(map[i][j] == 9){
                bx = i;
                by = j;
                map[i][j] = 0;
            }
        }
    }

    int flag = 0;

    while(1){
        memset(visited, 0, sizeof(visited));
        bfs(bx, by, 0);
        if(fish == 0){
            break;
        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(visited[i][j] == eatDistance && map[i][j] == 0){
                    bx = i;
                    by = j;
                    eat += 1;
                    sum += eatDistance;
                    map[by][bx] = 0;
                    flag = 1;
                    if(eat == sz){
                        sz = sz + 1;
                        eat = 0;
                    }
                    break;
                }
            }
            if(flag == 1){
                break;
            }
        }
        flag = 0;
        fish = 0;
    }
    cout<<sum;
    return 0;
}
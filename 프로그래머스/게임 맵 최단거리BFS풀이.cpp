#include<vector>
#include<queue>
using namespace std;

int visit[101][101];
int dist[101][101];

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int cnt = 0;
int bfs(vector<vector<int>>maps, int y, int x){
    dist[0][0] = 1;
    queue<pair<int,int>> q;
    q.push(make_pair(x, y));
    visit[0][0] = 1;
    while(!q.empty()){
        int curX = q.front().first;
        int curY = q.front().second;
        q.pop();
        for(int i = 0; i < 4; i++){
            int nx = curX + dx[i];
            int ny = curY + dy[i];
            
            if(ny >= maps.size() || nx < 0){
                continue;
            }
            if(nx >= maps[0].size() || ny < 0){
                continue;
            }
            if(maps[ny][nx] == 0 || visit[ny][nx]){
                continue;
            }
            q.push(make_pair(nx, ny));
            visit[ny][nx] = 1;
            dist[ny][nx] = dist[curY][curX] + 1;
        }
    }
    if(dist[maps.size()-1][maps[0].size()-1] == 0){
        return -1;
    }else{
        return dist[maps.size()-1][maps[0].size()-1];
    }
}

int solution(vector<vector<int> > maps)
{
    int answer = 0;

    answer = bfs(maps, 0, 0);

    return answer;
}
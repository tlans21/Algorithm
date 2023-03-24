#include<vector>


using namespace std;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int visit[101][101];
int temp = 987654321;
int dfs(vector<vector<int>> maps,int y, int x, int cnt){    
    visit[y][x] = 1;
    if(y == maps.size()-1 && x == maps[0].size()-1){
        temp = min(temp, cnt);
        return 0;
    }

    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >= maps[0].size() || ny >= maps.size() || nx < 0 || ny < 0){
            continue;
        }
        if(visit[ny][nx] || maps[ny][nx] == 0){
            continue;
        }
        
        dfs(maps, ny, nx, cnt+1);
        visit[ny][nx] = 0;
    }
    return 0;
}

int solution(vector<vector<int>> maps)
{
    int answer = 0;
    visit[0][0] = true;
    dfs(maps, 0, 0, 1);
    if(temp == 987654321){
        return -1;
    }else{
        return temp;
    }
}
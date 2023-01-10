#include <string>
#include <vector>

using namespace std;
int visit[10];
int maxim = -1;
int dfs(vector<vector<int>> dungeons, int depth, int k){
    if(depth == dungeons.size()+1){
        return 0;
    }

    for(int i = 1; i <= dungeons.size(); i++){
        if(visit[i] == 0){
            int needstaminar = dungeons[i-1][0];
            int staminar = dungeons[i-1][1];
            if(k >= needstaminar && k >= staminar){
                visit[i] = 1;
                maxim = max(maxim, depth+1);
                dfs(dungeons, depth+1, k-staminar);
                visit[i] = 0;
            }
        }
    }
    return 0;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    dfs(dungeons, 0, k);
    answer = maxim;
    return answer;
}
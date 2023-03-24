#include<iostream>
#include<queue>
#include<algorithm>
#include<cstring>

using namespace std;

bool visited[512];
int map[3][3];
int t;

void column_trans(int col){
    for(int i =0; i < 3; i++){
        map[i][col] = (map[i][col] == 1 ? 0 : 1);
    }
}

void row_trans(int row){
    for(int i = 0; i < 3; i++){
        map[row][i] = (map[row][i] == 1 ? 0 : 1);
    }
}

void cross_trans(int dir){
    for(int i = 0; i < 3; i++){
        if(dir == 0){
            map[i][i] = (map[i][i] == 1 ? 0 : 1);
        }else{
            map[i][2-i] =(map[i][2-i] == 1 ? 0 : 1); 
        }
    }
}
int map_to_int(){
    int value = 0;
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            value = value * 2 + map[i][j]; 
        }
    }
    return value;
}

void int_to_map(int number){
    for(int i = 2; i >=0; i--){
        for(int j = 2; j>=0; j--){
            map[i][j] = number % 2;
            number /= 2;
        }
    }
}

bool check(){
    char temp = map[0][0];
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(temp != map[i][j]){
                return false;
            } 
        }
    }
    return true;
}
int bfs(){
    
    queue<pair<int, int>> q;

    int first = map_to_int();
    q.push({first, 0});
    visited[first] = true;


    while(!q.empty()){
        int x = q.front().first;
        int cnt = q.front().second;
        q.pop();

        int_to_map(x);

        if(check()){
            return cnt;
        }
        
        for(int i = 0; i < 3; i++){
            column_trans(i); 
            int next = map_to_int();
            if(!visited[next]){
                visited[next] = true;
                q.push({next, cnt + 1});
            }
            column_trans(i);
        }

        for(int i = 0; i < 3; i++){
            row_trans(i); 
            int next = map_to_int();
            if(!visited[next]){
                visited[next] = true;
                q.push({next, cnt + 1});
            }
            row_trans(i);
        }
        for(int i = 0; i <= 1; i++){
            cross_trans(i);
            int next = map_to_int();
            if(!visited[next]){
                visited[next] = true;
                q.push({next, cnt + 1});
            }
            cross_trans(i);
        }
    }
    return -1;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>t;

    while(t--){
        memset(visited, false, sizeof(visited));
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                char data;
                cin>>data;
                if(data == 'H'){
                    map[i][j] = 1;
                }else{
                    map[i][j] = 0;
                }
            }
        }
        cout<<bfs()<<'\n';
    }

    return 0;
}
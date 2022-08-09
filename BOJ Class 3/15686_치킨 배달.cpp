#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>

#define MAX 50

using namespace std;

int N;
int M;
int map[MAX][MAX];
bool selcet[13];
int solution;

vector<pair<int, int>> house;
vector<pair<int, int>> chicken;
vector<pair<int, int>> a;

int Min(int A, int B) {
    if (A < B) {
        return A;
        } 
    return B; 
}


int DistanceSolve(){
    int sum = 0;
    for(int i = 0; i < house.size(); i++){
        int x = house[i].first;
        int y = house[i].second;
        int res = 1000000000;

        for(int j = 0; j <a.size(); j++){
            int x1 = a[j].first;
            int y1 = a[j].second;
            int dist = abs(x1 - x) + abs(y1 - y);
            res = Min(res, dist);
        }
        sum += res;
    }
    return sum;
}

void DFS(int idx, int cnt){
    if(cnt == M){
        solution = Min(solution, DistanceSolve());
        return;
    }

    for(int i = idx; i < chicken.size(); i++){
        if(selcet[i] == true){
            continue;
        }
        selcet[i] = true;
        a.push_back(chicken[i]);
        DFS(i, cnt + 1);
        selcet[i] = false;
        a.pop_back();
    }
}
void answer(){
    DFS(0, 0);
    cout<<solution<<endl;
}

int main(){
    solution = 10000000;
    cin>>N>>M;
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> map[i][j];
            if(map[i][j] == 1){
                house.push_back(make_pair(i, j));
            }
            if(map[i][j] == 2){
                chicken.push_back(make_pair(i, j));
            }
        }
    }
    answer();
}
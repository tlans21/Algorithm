#include<iostream>
#include<algorithm>

using namespace std;

int map[1001][3];
int N;
int cost[3];

int main(){
    
    cin>>N;
    map[0][1] = 0;
    map[0][2] = 0;
    map[0][0] = 0;


    for(int i = 1; i <= N; i++){
        cin >> cost[0] >> cost[1] >> cost[2];
        map[i][0] = min(map[i-1][1], map[i-1][2]) + cost[0];
        map[i][1] = min(map[i-1][0], map[i-1][2]) + cost[1];
        map[i][2] = min(map[i-1][0], map[i-1][1]) + cost[2];
        }
        cout << min(map[N][2], min(map[N][0], map[N][1]));
}
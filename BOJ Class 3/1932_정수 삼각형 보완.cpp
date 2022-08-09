#include<iostream>
#include<algorithm>

using namespace std;

int map[502][502] = {0};
int main(){
    int n;
    cin >> n;

    for(int i = 1; i <= n; i++){
        for(int j = 0; j <=i; j++){
            cin>>map[i][j];
        }
    }

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= i; j++){
            map[i][j] += max(map[i-1][j-1], map[i-1][j]);
        }
    }

    //마지막 값 비교
    int max = 0;
    for(int i = 1; i <= n; i++){
        if(max < map[n][i]){
            max = map[n][i];
        } 
    }
    cout << max;

    return 0;
 
}
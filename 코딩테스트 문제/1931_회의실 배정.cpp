#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<pair<long long, long long>> arr;

int main(){
    int N;
    cin>>N;

    for(int i = 0; i < N; i++){
        long long temp1;
        long long temp2;
        cin>>temp1>>temp2;
        arr.push_back({temp2, temp1});
    }

    sort(arr.begin(), arr.end());

    //러닝 타임이 중요한게 아니라, 누가 제일 먼저 끝나냐가 중요하다

    int cnt = 0;
    int time = 0;
    for(int i = 0; i < N; i++){
        if(time <= arr[i].second){
            time = arr[i].first;
            cnt++;
        }
    }
    cout<<cnt;
    return 0;
}
#include<iostream>

using namespace std;

int main(){
    int N;
    int K;
    int sum = 0;

    cin>> N >> K;
    int arr[10];

    for(int i = 0; i < N; i++){
        //동전 종류 입력
        cin>>arr[i];
    }

    for(int i = N-1; i >= 0; i--){
        if(arr[i] <= K){
          int coin = K / arr[i]; //동전 개수 갱신
          sum +=coin;
          if(K % arr[i] == 0){
            //딱 떨어진 경우
            cout<<sum;
            return 0;
          }else{
            K -= coin * arr[i];
          }
        } 
    }
    return 0;
}
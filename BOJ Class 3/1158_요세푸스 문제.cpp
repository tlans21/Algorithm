#include <iostream>
using namespace std;

int main(){
    int N;
    int K;
    int arr[5001];
    int cnt = 0;
    int printcnt;
    cin >> N >> K;

    for(int i = 1; i <= N; i++){
        arr[i] = i;
    }
    cout<<"<";

    while(N > 0){
        cnt = (cnt + K) % N;
        if(cnt == 0){
            cnt = N;
        }
        if(N == 1){
            cout<<arr[1]<<">";
        }
        else{
            cout<<arr[cnt]<<", ";
            for(int i = cnt; i < N; i++){
                arr[i] = arr[i + 1];
            }
            cnt -= 1;
        }
        N -= 1;
    }
    return 0;
}
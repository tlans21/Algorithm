#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    //idea 운동기구의 개수가 홀수일 경우와
    //짝수일 경우를 분리합니다.

    int N;

    cin>>N;
    long long arr[10000];
    long long max = 0;
    for(int i = 0; i < N; i++){
        cin>>arr[i];
    }
    sort(arr, arr+N);
    

    if(N % 2 == 0){
        for(int i = 0; i < N/2; i++){
            long long hap = arr[i] + arr[N-1-i];
            if(max < hap){
                max = hap;
            }
        }
        cout<<max;
        return 0;
    }

    if(N % 2 == 1){
        for(int i = 0; i < (N-1)/2; i++){
            long long hap2 = arr[i] + arr[N-2-i];
            if(max < hap2){
                max = hap2;
            }
        }
        if(max >= arr[N-1]){
            cout<<max;
            return 0;
        }else{
            cout<<arr[N-1];
            return 0;
        }
    }
    return 0;
}
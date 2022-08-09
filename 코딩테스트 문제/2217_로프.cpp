#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int N;
    int arr[100001];
    int mini = 1000000;
    int idx;
    int max = 0;
    int sol = 0;
    cin>>N;

    for(int i = 0; i < N; i++){
        cin>>arr[i];
    }

    sort(arr, arr+N, greater<>());

    for(int i = 1; i <= N; i++){
       sol = arr[i-1] * i;
       if(max < sol){
        max = sol;
       }
    }

    cout<<max;


    return 0;
}
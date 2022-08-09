#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int N;
    cin>>N;
    int arr[N];
    int sum = 0;
    for(int i = 0; i < N; i++){
        cin>>arr[i];
        sum += arr[i];
    }

    sort(arr, arr+N, greater<>());

    int core = N / 3;

    for(int i = 1; i <= core; i++){
        sum -= arr[3*i-1];
    }
    cout<<sum;
}
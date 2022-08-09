#include<iostream>
#include<algorithm>
using namespace std;

int main(){

    int N;

    cin>>N;

    int arr[N];
    
    
    for(int i = 0 ; i < N; i++){
        cin>>arr[i];
    }
    sort(arr, arr+N, greater<>());
    double sum;
    sum=arr[0];

    for(int i = 1; i < N; i++){
        sum += arr[i] / 2.0;
    }
    cout<<sum<<endl;
}
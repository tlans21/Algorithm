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
    }

    sort(arr, arr+N);

    int temp = 0;

    for(int i = 0; i < N; i++){
        temp += arr[i];
        sum += temp;
    }

    cout<<sum;
    return 0;
}
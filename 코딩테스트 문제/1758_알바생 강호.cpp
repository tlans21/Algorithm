#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    long long int N;
    cin>>N;
    long long int arr[N];
    long long int sum = 0;
    for(int i = 0; i < N; i++){
        cin>>arr[i];
    }

    sort(arr, arr+N, greater<>());

    for(int i = 0; i < N; i++){
        long long int temp = (arr[i] - ((i+1) - 1));
        if(temp <= 0){
            temp = 0;
            sum += temp;
        }else{
            sum += temp;
        }

    }
    cout<<sum;

}
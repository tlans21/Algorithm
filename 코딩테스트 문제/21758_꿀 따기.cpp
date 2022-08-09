#include<iostream>

using namespace std;

long long prefix[100001];

int main(){
    int N;
    long long answer = 0;
    cin>>N;
    long long arr[100001];

    for(int i = 1; i <= N; i++){
        cin>>arr[i];
            prefix[i] = prefix[i-1] + arr[i];
    }
    prefix[0] = 0;
    //k는 벌통의 위치, 최대 값을 구하기 위함이므로
    //벌통은 멘 오른쪽or 왼쪽으로 고정된다.
    for(int k = 2; k < N; k++){
        answer = max(prefix[k] - prefix[1] + prefix[N-1] - prefix[k-1], answer);
        answer = max(prefix[N] - prefix[1] - arr[k] + prefix[N] - prefix[k], answer);
        answer = max(prefix[N-1] - arr[k] + prefix[k-1], answer);
    }
    cout<<answer;
    return 0;

}
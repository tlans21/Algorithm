#include<iostream>
#include<stdio.h>
#include<time.h>

using namespace std;
/*
int main(){
    clock_t start;
    clock_t end;
    double result;
    start = clock();
    


    long long K;
    long long N;
    long long maxi = 0;
    long long sum = 0;
    long long maxlength;
    long long res = 0;
    long long count = 0;

    cin>>K>>N;
    long long arr[10001];
    for(long long i = 0; i < K; i++){
        cin>>arr[i];
        maxi = max(arr[i], maxi);
    }

    // 몇 cm로 자를 것인지에 대한 경우
    // 각 원소마다 검사
    for(long long i = 1; i <= maxi; i++){
        sum = 0;
        for(long long j = 0; j < K; j++){
            count = arr[j] / i;
            sum +=count;
        }
        if(sum >= N){
            maxlength = i;
            res = max(maxlength, res);
        }else{
            break;
        }
    }
    cout<<res;
    
    end = clock();
    result = (double)(end-start);
    cout<<"result : " << (result) / CLOCKS_PER_SEC << "seconds" <<endl;
    printf("%f", result / CLOCKS_PER_SEC); 
}
*/


int main(){
    int K;
    int N;
    long long arr[100001];
    long long maxi = 0;
    cin>>K>>N;

    for(int i = 0; i < K; i++){
        cin>>arr[i];
        maxi = max(maxi, arr[i]);
    } // 랜선의 최대 길이를 구함.
    
    long long left = 1;
    long long right = maxi;
    long long mid;
    long long sum = 0;
    long long res = 0;
    long long count;
    while(left<=right){
        sum = 0;
        mid = (left + right) / 2;
        for(int i = 0; i < K; i++){
            count = arr[i] / mid;
            sum += count;
        }
        if(sum >= N){ // sum == N 인경우 
            left = mid+1;
            res = max(res, mid);
        }else if(sum < N){
            right = mid-1;         
        }

    }
    cout<<res<<'\n';
    return 0;
}
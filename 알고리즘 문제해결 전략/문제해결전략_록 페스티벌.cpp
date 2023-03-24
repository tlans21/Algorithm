#include<iostream>

using namespace std;

int main(){
    cout<<fixed;
    cout.precision(8);
    int arr[1001];
    int N;
    int L;
    int T;
    int day;
    int sum;
    
    int min;
    cin>>T;
    cin>>N>>L;
    while(T--){
        double res = 1000000;
        for(int i = 0; i < N; i++){
            cin>>arr[i];
        }
    for(int i = 0; i <N-L+1; i++){
        sum = 0;
        day = 1;
        for(int j = i; j < N; j++){
            sum += arr[j];
            if(day >= L){
                if(res > sum/(double)day){
                    res = sum/(double)day; // i부터 시작했을 때 평균의 최소
                }
            }
            day++;
        }
    }
    cout<<res<<'\n';
    }
    return 0;
}
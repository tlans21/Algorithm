#include<iostream>

using namespace std;

int main(){
    long long N;
    long long M;

    long long sum = 1;
    long long sum2 = 1; 
    cin>>N>>M;
    long long s = M;
    while(s>0){
        sum = 
    }
    for(int i = 1; i <= M; i++){
        sum2 *= s;
        sum2 = sum2 %1000000007;
        s--;
    }
    cout<<sum/sum2<<'\n';
}
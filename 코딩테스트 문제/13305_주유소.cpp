#include<iostream>

using namespace std;

int main(){
    long long N;
    long long Distance[N];
    long long Oil[N];
    long long loc = 0;
    long long min = 1000000001;
    long long max = 0;
    long long price = Oil[0] * loc;
    int sumdist = 0;
    cin>>N;
    
    for(int i = 0; i < N; i++){
        //인접 도시거리
        cin>>Distance[i];
    }

    for(int i = 0; i < N; i++){
        cin>>Oil[i];
    }
    sumdist = Distance[0];
    for(int i = 0; i < N; i++){
    
        if(Oil[i] > Oil[i+1]){
             
        }else{
            sumdist += Distance[i+1]
        }
    }

}
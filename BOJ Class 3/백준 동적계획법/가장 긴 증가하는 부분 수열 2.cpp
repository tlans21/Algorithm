#include<iostream>

using namespace std;
int cache[1000001];
int A[1000000];
int N;

int Lis(int start){
    int &ret = cache[start+1];

    if(ret != -1){
        return ret;
    }
    ret = 1;

    for(int next = start + 1; next < N; ++next){
        if(start == -1 || A[start] < A[next]){
            ret = max(ret, Lis(next) + 1);
        }
    }
    return ret;
}

int main(){

     cin >> N;
     for(int i = 0; i < N; i++){
         cin>>A[i];
         cache[i] = -1;
     }
     cache[N] = -1;
     cout<<Lis(-1)-1;
     return 0;
}
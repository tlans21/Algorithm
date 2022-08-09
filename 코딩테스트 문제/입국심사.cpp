#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
using namespace std;

long long int N;
long long int M;
vector<long long int> arr(N);
long long int answer;

void search(long long int left, long long int right){
    if(left > right){
        return;
    }
    long long int center = (left + right)/2 ;
    long long int sum = 0;
    for(int i = 0; i < arr.size(); i++){
        sum += center / arr[i];
    }

    if(sum >= M){
        answer = center;
        search(left, center-1);
    }else if(sum < M){
        search(center + 1, right);
    }
}

int main(){
    cin>>N>>M;
    long long int max1 = 0;
    for(int i = 0; i < N; i++){
        long long int tmp;
        cin>>tmp;
        arr.push_back(tmp);
        max1 = max(max1, tmp);
    }
    
    long long int maxtime = M * max1;
    search(0, maxtime);

    cout<<answer;
}
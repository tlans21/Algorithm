#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


int N;
int ans;
int arr1[10000];
int M;


long long sum;

void search(int left, int right, int M){
    if(left > right){
        return;
    }
    sum = 0;
    int center = (left + right) / 2;
    for(int i = 0; i < N; i++){
      sum += min(arr1[i], center);
    }

    if(sum <= M){
        ans = center;
        search(center+1, right, M);        
    }else{
        search(left, center-1, M);
    }
}

int main(){
    ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

    int max1 = 0;
    cin>>N;
    for(int i = 0; i < N; i++){
        cin >> arr1[i];
        max1 = max(max1, arr1[i]);
    }
    cin>>M;
    search(0, max1, M);
    cout<<ans;
    return 0;
}
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N;
int M;

int main(){
    int point;
    cin>>N>>M;
    vector<int> a(N);

    for(int i = 0; i < N; i++){
        cin>>a[i];
    }
    sort(a.begin(), a.end());

    for(int j = 0 ; j < M; j++){
        int x;
        int y;
        cin>>x>>y;
        point = upper_bound(a.begin(), a.end(), y)-lower_bound(a.begin(), a.end(), x);
        cout<<point<<'\n';    
    }
    return 0;
}
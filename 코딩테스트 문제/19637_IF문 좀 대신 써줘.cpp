#include<iostream>
#include<vector>

using namespace std;

int main(){
    std::ios::sync_with_stdio(false);
	cin.tie(0);
    int N;
    int M;
    vector<string> s;
    vector<int> a;

    cin>>N>>M;

    for(int i = 0; i < N; i++){
        string y;
        int x;
        cin>>y>>x;
        s.push_back(y);
        a.push_back(x);
    }

    for(int i = 0; i < M; i++){
        int index;
        int x;
        cin>>x;
        cout<<s[lower_bound(a.begin(), a.end(), x) - a.begin()]<<'\n'; 
    }
    return 0;


}

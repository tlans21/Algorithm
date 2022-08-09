#include<iostream>
#include<vector>
#include<stack>

using namespace std;

stack<pair<int,int>> s;
int N;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);


    cin >> N;

    for(int i = 1; i <= N; i++){
        int temp;
        cin>>temp;
        while(!s.empty()){
            if(s.top().second > temp){
                cout<<s.top().first<<" ";
                break;
            }
            s.pop();
        }
        if(s.empty()){
            cout<<0<<" ";
        }
        s.push({i, temp});
    }
    return 0;
}
#include<iostream>
#include<vector>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int N;

    cin>>N;

    vector<int> vec[100002];
    for(int i = 0; i < N-1; i++){
        int a;
        int b;
        cin>>a>>b;
        vec[a].push_back(b);
        vec[b].push_back(a);
    }
    
    int question;

    cin>>question;

    for(int s = 0; s < question; s++){
        int t;
        int k;

        cin>>t>>k;
        //정점이 단절점인지?
        if(t == 1){
            int cnt = vec[k].size();
            if(cnt >=2){
                cout<<"yes"<<'\n';
            }else{
                cout<<"no"<<'\n';
            }
        }else if(t == 2){
            //간선이 단절선인지?
            int cnt2 = vec[k].size();
            if(cnt2 >=1){
                cout<<"yes"<<'\n';
            }else{
                cout<<"no"<<'\n';
            }
        }
    }
    return 0;
}
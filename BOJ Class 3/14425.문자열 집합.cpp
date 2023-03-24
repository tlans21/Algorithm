#include<iostream>
#include<map>
using namespace std;

int main(){
    int N;
    int M;
    int cnt = 0;
    cin>>N>>M;
    string str;
    string str1;
    map<string, bool> m;
    for(int i = 0; i < N; i++){
        cin>>str;
        m[str] = true;
    }

    for(int i = 0; i < M; i++){
        cin>>str1;

        if(m[str1]){
            cnt++;
        }
    }

    cout<<cnt<<endl;

    return 0;
}
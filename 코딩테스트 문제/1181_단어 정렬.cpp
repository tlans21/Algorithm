#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

bool compare(string a, string b){
    if(a.length() == b.length()){
        return a < b;
    }else(a.length() < b.length()){
        return true;
    }
}
int main(){
    
    int N;

    cin>>N;

    vector<string> arrstr;

    for(int i = 0; i < N; i++){
        string str;
        cin>>str;
        if(find(arrstr.begin(), arrstr.end(), str) == arrstr.end()){
            arrstr.push_back(str);
        }
    }
    sort(arrstr.begin(), arrstr.end(), compare);

    // 반복자 선언 iterator는 포인터로 보면 된다.
    for(vector<string>::iterator iter = arrstr.begin(); iter < arrstr.end(); iter++){
        cout<<*iter<<'\n';
    }
    return 0;
}

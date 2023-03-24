#include<iostream>

using namespace std;

int main(){
    
    string str;

    getline(cin, str);
    
    int cnt = 0;
    // 공백 문자가 하나만 있는 경우
    if(str.empty()){
        cout<<cnt;
    }
    //이외의 경우
    cnt = 1;
    for(int i = 0; i < str.length(); i++){
        if(str[i] == ' '){
            cnt++;
        }
    }
    //
    if(str[0] == ' '){
        cnt = cnt - 1;
    }
    if(str[str.length()-1] == ' '){
        cnt = cnt - 1;
    }
    cout<<cnt;
    return 0;
}
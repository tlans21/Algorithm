#include<iostream>
#include<algorithm>
#include<stack>

using namespace std;

int main(){
    stack<char> s;
    string str;
    getline(cin, str);

    for(int i = 0; i < str.length(); i++){
        if(str[i] == '<'){
            while(!s.empty()){
                cout<<s.top();
                s.pop();
            }
            while(1){
                cout<<str[i];
                if(str[i] == '>'){
                    break;
                }
                i++;
            }
        }else if(str[i] ==' '){
            while(!s.empty()){
                cout<<s.top();
                s.pop();
            }
            cout<<' ';
        }
        else{
            s.push(str[i]);
        }
    }

    while(!s.empty()){
        cout<<s.top();
        s.pop();
    }

    return 0;
}
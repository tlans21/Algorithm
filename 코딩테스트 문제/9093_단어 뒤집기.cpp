#include<iostream>
#include<stack>
#include<string>

using namespace std;

int main(){
    int T;
    string str;
    stack<char> s;
    string answer ="";
    cin>>T;
    cin.ignore();
    for(int i = 0; i < T; i++){
        getline(cin, str);
        str += ' ';

        for(int j = 0; j < str.length(); j++){
            char spell = str[j];
            if(spell == ' '){
                while(!s.empty()){
                    cout<<s.top();
                    s.pop();
                }
                cout<<spell;
            }else{
                s.push(spell);
            }
        }
        cout<<'\n';
    }
    return 0;
}
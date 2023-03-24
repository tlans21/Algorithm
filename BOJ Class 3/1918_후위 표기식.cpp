#include<iostream>
#include<stack>
#include<string>

using namespace std;

int main(){
    string s;
    stack<char> square;

    cin>>s;

    for(int i = 0; i < s.length(); i++){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            cout<< s[i];
        }
        else{
            if(s[i] == '('){
                square.push(s[i]);
            }else if(s[i] == '*' || s[i] == '/'){
                while(!square.empty() && (square.top() == '*' || square.top() == '/')){
                            cout<<square.top();
                            square.pop();
                }
                square.push(s[i]);
            }else if(s[i] == '+' || s[i] == '-'){
                while(!square.empty() && square.top() != '('){
                        cout<<square.top();
                        square.pop();
                }
                square.push(s[i]);
            }else if(s[i] == ')'){
                while(!square.empty() && square.top() != '('){
                        cout<<square.top();
                        square.pop();
                }
                square.pop();
            }    
        }
    }
    while(!square.empty()){
        cout<<square.top();
        square.pop();
    }

    return 0;
}
#include<iostream>
#include<string>
#include<algorithm>

using namespace std;


int main(){
    string str;
    string boom;
    string sub ="";
    bool flag;
    cin>>str>>boom;
    int str_length = str.length();
    int boom_length = boom.length();
    for(int i = 0; i < str.length(); i++){
        sub += str[i];
        flag = true;
        if(sub.length() >=boom_length){
            for(int j = 0; j < boom_length; j++){
                if(sub[sub.length()-boom_length+j] != boom[j]){
                    flag = false;
                    break;
                }
            }
            if(flag){
                sub.erase(sub.end() - boom_length, sub.end());
            }
        }
    }   
    if(sub.empty()){
        cout<<"FRULA"<<'\n';
    }else{
        cout<<sub<<'\n';
    }
    return 0;
}
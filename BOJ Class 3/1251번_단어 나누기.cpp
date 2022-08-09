#include<iostream>
#include<string>
using namespace std;

string str;
string better;

int main(){
    better = '{';
    cin >> str;

    for(int i = 0; i < str.size()-2; i++){
        for(int j = i+1; j < str.size()-1; j++){

            string a;
            for(int u = i; u >= 0; u--){
                a += str[u];
            }
            for(int u = j; u > i; u--){
                a += str[u];
            }
            for(int u = str.size()-1; u > j; u--){
                a+= str[u];
            }
            if(better > a){
                better = a;
            }
        }
    }

    cout<<better;
}
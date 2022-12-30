#include<iostream>

using namespace std;

int main(){
    string input;
    int cnt = 0;
    cin>>input;
    for(int i = 0 ; i < input.length(); i++){
        if(cnt == input.length()-1){
            cout<<"0"<<'\n';
            return 0;
        }

        if(input[i] == input[i+1]){
            cnt++;
        }
    }
    
    int ZeroCnt = 0;
    int OneCnt = 0;
    for(int i = 0; i < input.length(); i++){
        if(i == input.length()-1){
            if(input[i] == '1'){
                OneCnt++;
            }else if(input[i] == '0'){
                ZeroCnt++;
            }
        }else{
            if(input[i] == '0'){
                if(input[i+1] == '1'){
                    ZeroCnt++;
                }
            }else if(input[i] == '1'){
                if(input[i+1] == '0'){
                    OneCnt++;
                }
            }
        }
    }
    
    if(ZeroCnt > OneCnt){
        cout<<OneCnt<<'\n';
    }else{
        cout<<ZeroCnt<<'\n';
    }
    return 0;
}
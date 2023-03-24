#include<iostream>

using namespace std;

int main(){
    string str;

    cin>>str;
    int Mcnt = 0;
    int Kcnt = 0;
    for(int i = 0; i < str.length(); i++){
        int temp = str[i];

        if(temp == 'K'){
            cout<<5;
            for(int j = 0; j < Mcnt; j++){
                cout<<0;
            }
            Mcnt = 0;
        }else if(temp == 'M'){
            Mcnt++;
        }
    }
    
    for(int i = 0; i < Mcnt; i++){
        cout<<1;
    }

    cout<<'\n';
    Mcnt = 0;
    Kcnt = 0;

    for(int i = 0; i < str.length(); i++){
        int temp1 = str[i];
        if(temp1 == 'K'){
            cout<<5;
            Mcnt = 0;
        }else if(temp1 == 'M'){
            Mcnt++;
            if(Mcnt == 1){
                cout<<1;
            }else{
                cout<<0;
            }
        }
    }
    return 0;
}
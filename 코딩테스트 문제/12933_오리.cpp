#include<iostream>
#include<string>


using namespace std;

int main(){
    string str;
    int kflag = 0;
    int cnt = 0;
    //q, u, a, c, k가 서로 상쇄되어 결국 0개로 남아있어야함.
    int arr[6] = {0, 0, 0, 0, 0, 0};
    int n;
    cin>>str;

    for(int i = 0; i < str.length(); i++){
        //처음에는 무조건 q로 시작해야한다.
        //아닐 시 이상한 녹음으로 판명

        if(str[i] == 'q'){
            n = 1;
        }
        
        if(str[i] == 'u'){
            n = 2;
        }
        
        if(str[i] == 'a'){
            n = 3;
        }
        
        if(str[i] == 'c'){
            n = 4;
        }
        
        if(str[i] == 'k'){
            n = 5;
        }
    
        if(str[0] != 'q'){
            cout<<-1;
            return 0;    
        }
        if(str[i] == 'k'){
            kflag++;
        }
        //문자열이 k인 인덱스가 아직 안온 상태
        if(str[i] == 'q' && !kflag){
            cnt++;
        }

        if(str[i] == 'q' && kflag){
            kflag--;  
        }

        arr[n]++;
        arr[n-1]--;
        
        for(int j = 1; j < 5; j++){
            if(arr[j]<0){
                cout<<-1;
                return 0;
            }
        }
    }

    if(str.length() % 5 != 0){
        cout<<-1;
        return 0;
    }

    for(int j = 1; j < 5; j++){
        if(arr[j] != 0){
            cout<<-1;
            return 0;
        }
    }

    cout<<cnt;
    return 0;
}
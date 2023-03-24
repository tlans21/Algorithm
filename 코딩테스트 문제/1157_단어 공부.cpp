#include<iostream>

using namespace std;

int main(){
    
    string str;
    int arr[26] = {0};
    cin>>str;

    

    for(int i = 0; i <= str.length()-1; i++){
        for(int j = 'a'; j <= 'z'; j++){
            if(str[i] == j){
                arr[j-'a']++;
            }
        }
    }
    
    for(int i = 0; i <= str.length()-1; i++){
        for(int j = 'A'; j <= 'Z'; j++){
            if(str[i] == j){
                arr[j-'A']++;
            }
        }
    }

    int max = 0;
    int maxidx;

    for(int i = 0; i <= 25; i++){
        if(arr[i] > max){
            max = arr[i];
            maxidx = i;
        }
    }

    int cnt = 0;

    for(int k = 0; k <=25; k++){
        if(arr[k] == max){
            cnt++;
        }
    }

    if(cnt >= 2){
        cout<<"?"<<'\n';
    }else if(cnt == 1){
        printf("%c", maxidx+'A');
    }
    return 0;
}
#include<iostream>
#include<string>

using namespace std;

int main(){
    char SL;
    char SR;
    bool flag = false;
    string input;
    int cnt = 0;
    int arr[26][2] = { {1, 2}, {5, 3}, {3, 3}, {3, 2}, {3, 1}, {4, 2}, {5, 2},
	{6, 2}, {8, 1}, {7, 2}, {8, 2}, {9, 2}, {7, 3}, {6, 3}, {9, 1}, {10, 1},
	{1, 1}, {4, 1}, {2, 2}, {5, 1}, {7, 1}, {4, 3}, {2, 1}, {2, 3}, {6, 1},
	{1, 3} };

    char answer[15] = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v'};

    cin>>SL>>SR;
    cin>>input;

    for(int i = 0; i < input.length(); i++){
        //순번대로 오는 문자가 모음인지 자음인지 판별하여 구분
        for(int j = 0; j < 15; j++){
            if(input[i] == answer[j]){
                flag = true; // 자음
                break;
            }
        }

        if(flag){
            if(input[i]==SL){
                cnt += 1; //타자 입력
            }else{
                cnt+=abs(arr[SL-'a'][0]-arr[input[i] - 'a'][0])+abs(arr[SL-'a'][1]-arr[input[i]-'a'][1]);
                cnt+= 1; //타자 입력
                SL = input[i]; // 현재 손 위치
            }
        }else{
            if(input[i]==SR){
                cnt += 1; //타자 입력
            }else{
                cnt+=abs(arr[SR-'a'][0]-arr[input[i] - 'a'][0])+abs(arr[SR-'a'][1]-arr[input[i]-'a'][1]);
                cnt += 1; //타자 입력
                SR = input[i]; // 현재 손 위치
            }
        }
        flag = false; //기본값으로 다시 세팅
    }

    cout<<cnt;
}
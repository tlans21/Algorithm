#include<iostream>

using namespace std;

int main(){
    int arr[26] ={0};
    string str;

    /*cin>>str;*/

    /*  for(int i = 0; i <= 25; i++){
            arr[i] = -1;
        }

        for(int i = 'a'; i <= 'z'; i++){
            for(int j = 0; j <= str.length(); j++){
                if(str[j] == i){
                    arr[i-'a'] = j;
                    break;
                }
            }
        }
    */

    for(int i = 0; i <= 25; i++){
        cout<<arr[i]<<' ';
    }

    return 0;
}
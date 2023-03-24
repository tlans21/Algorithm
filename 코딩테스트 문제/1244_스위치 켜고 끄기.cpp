#include<iostream>

using namespace std;

int main(){
    int N;
    int studentNum;
    int situation[101];
    int sex;
    int button;

    cin>>N;
    for(int i = 1; i <= N; i++){
        cin>>situation[i];
    }

    cin>>studentNum;

    for(int i = 0; i < studentNum; i++){
        cin>>sex>>button;

        if(sex == 1){
            for(int j = 1; j <= N; j++){

                if(j % button == 0){
                  situation[j] =!situation[j];
                }
            }
        }

        else if(sex == 2){
           situation[button] =!situation[button];
           for(int i = 1; i <= N; i++){
            if(situation[button - i] == situation[button + i]){

                if(button + i > N || button - i < 1){
                    break;
                }
                situation[button - i] =!situation[button - i];
                situation[button + i] =!situation[button + i];
            }
            else{
                break;
            }
           }
        }
    }

    for(int i = 1 ; i <= N; i++){
        cout<<situation[i]<<' ';
        if(i%20 == 0){
            cout<<'\n';
        }
    }
   
    return 0;
}
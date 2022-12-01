#include<iostream>

using namespace std;

int main(){
    int H;
    int W;
    int N;
    int TC;

    cin>>TC;

    int room;
    int floor;
    while(TC>0){
        cin>>H>>W>>N;
        for(int i = 1; i <= W; i++){
            
            

            room = N/H;
            floor = N%H; 
            if(room ==  i){
                if(floor == 0){
                    printf("%d%02d\n", H, room);
                }else{
                    printf("%d%02d\n", floor, room+1);
                } 
            }
        }
        TC--;
    }
    return 0;   
}
#include<iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

typedef struct point{
    int x;
    int y;
}point;

void qsort(point arr[], int L ,int R){
    int left = L; 
    int right = R;
    point pivot = arr[(L+R)/2];
    
    point temp;

    do{
        while(arr[left].x < pivot.x){
            left++;
        }
        while(arr[left].x == pivot.x){
            if(arr[left].y < pivot.y){
                left++;
            }else{
                break;
            }
        }
        while(arr[right].x > pivot.x){
            right--;
        }
        while(arr[right].x == pivot.x){
            if(arr[right].y > pivot.y){
                right--;
            }else{
                break;
            }
        }
        
        if(left <= right){
            temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }while(left <= right);

    if(L < right){
        qsort(arr, L, right);
    }
    if(left < R){
        qsort(arr, left, R);
    }
}

int main(){
    int N;
    
    cin>>N;
    point arr1[100001]={0};
    for(int i = 0; i < N; i++){
       cin>>arr1[i].x>>arr1[i].y; 
    }
    qsort(arr1, 0, N-1);
    for(int i = 0; i < N; i++){
        cout<<arr1[i].x<<' '<<arr1[i].y<<'\n';
    }
    
    return 0;
}
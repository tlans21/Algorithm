#include <bits/stdc++.h>
#include<iostream>
#include<algorithm>


#define MAX 100001
using namespace std;

int arr1[MAX][4];
int dp[4];
int dp2[4];
int m1;
int m2;
int m3;



int main(){
    int N;

    cin >> N;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= 3; j++){
        cin>>arr1[i][j];
        }
    }
    for(int i = 1; i <= 4; i++){
        dp[i] = arr1[1][i];
    }


    for(int i = 2; i <= N; i++){
      

        
        dp[1] = arr1[i][1] + max(dp[1],dp[2]);
        dp[2] = arr1[i][2] + max({dp[1], dp[2], dp[3]});
        dp[3] = arr1[i][3] + max(dp[1], dp[2]);
    }
    int solution = max({dp[1], dp[2], dp[3]});
    cout<<solution<<' ';
     for(int i = 1; i <= 4; i++){
        dp2[i] = arr1[1][i];
    }


    for(int i = 2; i <= N; i++){
      
        dp2[1] = arr1[i][1] + min(dp2[1], dp2[2]);
        dp2[2] = arr1[i][2] + min({dp2[1], dp2[2], dp2[3]});
        dp2[3] = arr1[i][3] + min(dp[2], dp[3]);
    }

    

    int solution2 = min({dp2[1], dp2[2], dp2[3]});
    
    cout<<solution2;


    return 0;
}
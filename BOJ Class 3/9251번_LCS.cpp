#include<iostream>
#include<algorithm>

using namespace std;

int LCS[1001][1001];

int main(){
    string str1;
    string str2;
    cin>>str1;
    cin>>str2;
    int maxi = 0;

    for(int i = 1; i <= str1.length(); i++){
        for(int j = 1; j <= str2.length(); j++){
            if(str1[i-1] == str2[j-1]){
                LCS[i][j] = LCS[i-1][j-1] + 1;
            }else{
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]);
            }
        }
    }
    for(int i = 1; i <= str1.length(); i++){
        for(int j =1; j <= str2.length(); j++){
            if(maxi < LCS[i][j]){
                maxi = LCS[i][j];
            }
        }
    }
    cout<<maxi;
}
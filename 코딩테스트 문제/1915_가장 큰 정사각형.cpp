#include<iostream>
#include<algorithm>

using namespace std;


int dp[1002][1002];

int main(){
    int N;
    int M;
    cin>>N>>M;

    string str;

    for(int i = 1; i <= N; i++){
        cin>>str;
        for(int j = 0; j < str.length(); j++){
            dp[i][j+1] = str[j] - '0';
        }
    }

    int answer = 0;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= M; j++){
            if(dp[i][j] == 1){
                dp[i][j] = 1 + min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]});
                answer = max(dp[i][j], answer);
            }
        }
    }
    
    int solution = answer * answer;
    cout<<solution;
    return 0;
}
#include<iostream>
#include<cmath>
using namespace std;



int main(){
    ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
    int T;
    int N;
    int M;
    cin>>T;

    long long answer = 0;

    while(T--){
        long long dp[12][2002] = {0,};
        cin>>N>>M;
        answer = 0;
        dp[0][0] = 1;
        int st = 1;
        int max_m = M /(int)pow(2, N-1);
        
        for(int i = 1; i <= max_m; i++){
            dp[1][i] = 1;
        }

        for(int i = 2; i <= N; i++){
            st *= 2;
            max_m = M / (int)pow(2, N-i);
            for(int j = st; j <= max_m; j++){
                int pre_m = j / 2;
                for(int k = st/2; k <= pre_m; k++){
                    dp[i][j] += dp[i-1][k];
                }
            } 
        }

        for(int i = 0; i <= M; i++){
            answer += dp[N][i];
        }
        cout<<answer<<'\n';
    }
    return 0;   
}
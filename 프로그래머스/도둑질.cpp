#include <string>
#include <vector>

using namespace std;

int DP[1000010];
int DP2[1000010];
int solution(vector<int> money) {
    int answer = 0;
    
    int n = money.size()-1;
    
    DP[0] = money[0];
    DP[1] = DP[0];
    DP2[0] = 0;
    DP2[1] = money[1];

    for(int i = 2; i < n; i++){
        DP[i] = max(DP[i-2] + money[i], DP[i-1]);
    }
    for(int i = 2; i <= n; i++){
        DP2[i] = max(DP2[i-2] + money[i], DP2[i-1]);
    }

    answer = max(DP[n-1], DP2[n]);
    
    return answer;
}
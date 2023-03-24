#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;

    int maxValue;
    int minValue;
    int G = 0;
    int S = 0;
    for(int i = 0; i < sizes.size(); i++){
        maxValue = max(sizes[i][0], sizes[i][1] ); 
        minValue = min(sizes[i][0], sizes[i][1]);

        G = max(maxValue, G);
        S = max(minValue, S);  
    }
    answer = G * S;
    return answer;
}
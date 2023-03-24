#include <string>
#include <vector>

using namespace std;

int solution(vector<int> ingredient) {
    int answer = 0;
    
    int cur = 0;
    int size = ingredient.size() - 3;
    while(cur < size){
        if(ingredient[cur] == 1 && ingredient[cur+1] == 2 && ingredient[cur+2] == 3 && ingredient[cur+3] == 1){
            answer++;
            ingredient.erase(ingredient.begin() + cur, ingredient.begin() + cur + 4);
            cur = max(cur - 4, -1);
            size = ingredient.size() - 3;
        }
        
        cur++;
    }
    return answer;
}
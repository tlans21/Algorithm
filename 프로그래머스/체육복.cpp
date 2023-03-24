#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int visit[101] ={0};
int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int cnt = 0;
      for(int i = 0; i < lost.size(); i++){
        for(int j = 0; j < reserve.size(); j++){
            if(lost[i] == reserve[j]){
                lost.erase(lost.begin() + i);
                reserve.erase(reserve.begin() + j);
                i = -1;
                break;
            }
        }
    }
    sort(lost.begin(),lost.end());
    sort(reserve.begin(),reserve.end());
    
    for(int i = 0; i < reserve.size(); i++){
        int reserveNum = reserve[i];
        int reservePlus = reserveNum + 1;
        int reserveMinus = reserveNum - 1;
        for(int j = 0; j < lost.size(); j++){
            if(lost[j] == reserveMinus || lost[j] == reservePlus){
                lost.erase(lost.begin() + j);
                break;
            }
        }
    }
    answer = n - lost.size();
    return answer;
}
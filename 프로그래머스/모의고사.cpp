#include <string>
#include <vector>

using namespace std;
int map1[10] = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5};
int map2[16] = {2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5};
int map3[20] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> one;
    vector<int> two;
    vector<int> three;

    while(one.size() != answers.size()){
        for(int i = 0; i < 10; i++){
            one.push_back(map1[i]);
            if(one.size() == answers.size()){
                break;
            }
        }
    }
    while(two.size() != answers.size()){
        for(int i = 0; i < 16; i++){
            two.push_back(map2[i]);
            if(two.size() == answers.size()){
                break;
            }
        }
    }
    while(three.size() != answers.size()){
        for(int i = 0; i < 20; i++){
            three.push_back(map3[i]);
            if(three.size() == answers.size()){
                break;
            }
        }
    }
    int cnt1 = 0;
    int cnt2 = 0;
    int cnt3 = 0;
    for(int i = 0; i < answers.size(); i++){
        if(one[i] == answers[i]){
            cnt1++;
        }
        if(two[i] == answers[i]){
            cnt2++;
        }
        if(three[i] == answers[i]){
            cnt3++;
        }
    }
    int temp;
    temp = max(max(cnt1, cnt2), cnt3);

    if(temp == cnt1){
        answer.push_back(1);
    }
    if(temp == cnt2){
        answer.push_back(2);
    }
    if(temp == cnt3){
        answer.push_back(3);
    }



    return answer;
}
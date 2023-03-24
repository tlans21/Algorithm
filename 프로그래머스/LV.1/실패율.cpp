#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int compare(pair<double, int>&a, pair<double, int> &b){
    if(a.first == b.first){
        return a.second < b.second;
    }
        return a.first > b.first;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<double, int>> v;
    int entire;
    int nonpass;
    for(int i = 1; i <= N; i++){
        entire = 0;
        nonpass = 0;
        for(int j = 0; j < stages.size(); j++){
            if(stages[j] >= i){
                entire++;
                if(stages[j] == i){
                    nonpass++;
                }
            }
        }
        if(entire == 0){
            v.push_back({0, i});
            continue;
        }
        double t = (double)nonpass/entire;
        v.push_back({t, i});
    }
    sort(v.begin(), v.end(), compare);
    for(int i = 0; i < v.size(); i++){
        answer.push_back(v[i].second);
    }
    return answer;
}
#include <string>
#include <vector>

using namespace std;

int solution(string dartResult) {
    vector<int> v;
    int answer = 0;
    int idx = 0;
    string num = "";
    for(int i = 0; i < dartResult.size(); i++){
        if(dartResult[i] >= '0' && dartResult[i] <= '9'){
            num += dartResult[i];
        }else if(dartResult[i] == 'S'){
            int n = stoi(num);
            v.push_back(n);
            num = "";
            idx++;
        }else if(dartResult[i] == 'D'){
            int n = stoi(num);
            v.push_back(n * n);
            num = "";
            idx++;
        }else if(dartResult[i] == 'T'){
            int n = stoi(num);
            v.push_back(n * n * n);
            num = "";
            idx++;
        }else if(dartResult[i] == '*'){
            if(idx == 1){
                v[idx-1] *=2; 
            }else{
                v[idx-1] *=2;
                v[idx-2] *=2;
            }
        }else if(dartResult[i] == '#'){
            v[idx - 1] *-=v[idx-1]; 
        }
    }
    for(int i = 0; i < v.size(); i++){
        answer += v[i];
    }
    return answer;
}
#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    bool flag = true;
    for(int i = 0; i <= discount.size()-10; i++){
        map<string, int> m;
        flag = true;
        for(int j = i; j < i+10; j++){
            if(m.find(discount[j]) != m.end()){
                m[discount[j]]++;
            }else{
                m.insert({discount[j], 1});
            }
        }
        for(int k = 0; k < number.size(); k++){
            if(m[want[k]] != number[k]){
                flag = false;
                break;
            }
        }
        if(flag == true){
            answer++;
        }
    }
    return answer;
}
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    string s = "";
    int cnt = 0;
    int cnt2 = 0;
    int temp = n;
    while(temp > 0){
        s += to_string(temp % 2);
        temp = temp / 2;
    }
    for(int i = 0; i < s.size(); i++){
        if(s[i] == '1'){
            cnt++;
        }
    }
    while(1){
        cnt2 = 0;
        string str = "";
        n++;
        int tempN = n;
        while(tempN > 0){
            str += to_string(tempN % 2);
            tempN = tempN / 2;
        }
        for(int i = 0; i < str.size(); i++){
            if(str[i] == '1'){
                cnt2++;
            }
        }
        if(cnt == cnt2){
            answer = n;
            break;
        }
    }
    return answer;
}
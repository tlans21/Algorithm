#include <string>
#include <vector>

using namespace std;

int solution(string numbers) {
    int answer = 0;
    bool flag = true;
    vector<int> num;
    
    for(int i = 0; i < numbers.size(); i++){
        int number = (numbers[i]) - '0';
        num.push_back(number);    
    }
    int cnt = 0;
    for(int i = 0; i < num.size(); i++){
        //첫번째 자리 검사
        int temp = num[i];
        for(int j = 2; j < temp; j++){
            if(temp % j == 0){
                flag = false;
            } 
        }
        if(flag == true){
            cnt++;
        }
        flag = true;
        for(int s = 0; s <num.size(); s++){
            if(s == i){
                continue;
            }
            temp += num[s];
            for(int k = 2; k < temp; k++){
                if(temp % k == 0){
                    flag = false;
                } 
            }
            if(flag == true){
                cnt++;
            }
            temp -= num[s];
            flag = true;
            for(int c = 0; c <num.size(); c++){
                if(c == i || c == s){
                    continue;
                }
                temp +=num[c];
                for(int q = 2; q < temp; q++){
                    if(temp % q == 0){
                        flag = false;
                    }
                }
                temp -= num[c];
                flag = true;
            }
        }
    }

    return answer;
}
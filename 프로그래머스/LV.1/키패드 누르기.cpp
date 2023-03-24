#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    int right = 10;
    int left = 12;
    for(int i = 0; i < numbers.size(); i++){
        if(numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7){
            left = numbers[i];
            answer += "L";
        }else if(numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9){
            right = numbers[i];
            answer += "R";
        }else{
            if(numbers[i] == 0){
                numbers[i] = 11;
            }
            int a = (abs(numbers[i] - left) / 3) + (abs(numbers[i] - left)) % 3;
            int b = (abs(numbers[i] - right) / 3) + (abs(numbers[i] - right)) % 3;
            if(a == b){
                if(hand == "right"){
                    right = numbers[i];
                    answer += 'R';
                }else if(hand == "left"){
                    left = numbers[i];
                    answer += 'L';
                }
            }else if(a > b){
                right = numbers[i];
                answer += 'R';
            }else if(a < b){
                left = numbers[i];
                answer += 'L';
            }
        }
    }
    return answer;
}
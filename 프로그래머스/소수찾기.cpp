#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_set>
using namespace std;

int check(int num){
    if(num == 0 || num == 1){
        return 0;
    }
    for(int i = 2; i <= sqrt(num); i++){
        if(num % i == 0){
            return 0;
        }
    }
    return 1;
}

int solution(string numbers) {
    int answer = 0;
    //소수가 만들어지는 경우의 수를 vector에 담는다 //순열 조합 오름차순
    // vector에 담긴 소수를 에라토스테네스의 체를 이용하여 카운트
    unordered_set<int> s;
    int temp = 0;
    sort(numbers.begin(), numbers.end());

    do
    {
        for(int i = 1; i <= numbers.size(); i++){
            temp = stoi(numbers.substr(0, i)); // substr을 통해 자른다.
            if(check(temp)){
                s.insert(temp);
            }
        }
    } while (next_permutation(numbers.begin(), numbers.end()));


    answer = s.size();
    return answer;
}
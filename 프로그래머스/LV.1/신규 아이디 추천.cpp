#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    string answer = "";
    
    //대문자를 소문자로
    // 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외
    // .가 2번 이상 연속된 부분을 하나의 마침표로 치환
    // .가 처음이나 끝에 위치한다면 제거
    // 빈문자열일 시 a로 대입
    //  16자 이상일 시 첫 15개의 문자를 제외한 나머지 문자 제거
    // 2자 이하라면 마지막문자를 3이 될때까지 끝에 붙인다.
    string temp = "";
    
    for(int i = 0; i < new_id.size(); i++){
        if(new_id[i] >= 'A' && new_id[i] <= 'Z'){
            new_id[i] = new_id[i] + 32; // 소문자로 치환
        }
        temp+= new_id[i];
    }
    
    string temp1 = "";
    for(int i = 0; i < temp.size(); i++){
        if(temp[i] >= 'a' && temp[i] <= 'z'){
            temp1 +=temp[i];
            continue;
        }
        if(temp[i] >= '0' && temp[i] <= '9'){
            temp1 +=temp[i];
            continue;
        }
        if(temp[i] == '-' || temp[i] == '_' || temp[i] == '.'){
            temp1 +=temp[i];
            continue;
        }
    }
    string temp2 = "";
    int dotcnt = 0;
    for(int i = 0; i < temp1.size(); i++){
        if(temp1[i] == '.'){
            dotcnt++;
            if(dotcnt > 1){
                continue;
            }
        }else if(temp1[i] != '.'){
            dotcnt = 0;
        }
        temp2 += temp1[i];
    }
    
    string temp3 = "";
    for(int i = 0; i < temp2.size(); i++){
        if(temp2[i] =='.' && i == 0){
            continue;
        }else if(temp2[i] == '.' && i == temp2.size()-1){
            continue;
        }
        temp3 +=temp2[i];
    }
    
    string temp4 = "";
    
    if(temp3.size() == 0){
        temp4 += 'a';
    }else{
        temp4 = temp3;
    }
    
    string temp5 = "";
    if(temp4.size() >= 16){
        for(int i = 0; i < 15; i++){
            if(i == 14 && temp4[i] == '.'){
                continue;
            }
            temp5 += temp4[i];
        }
    }else{
        temp5 = temp4;
    }
    if(temp5.size() <= 2){
        char str = temp5[temp4.size()-1];
        if(temp5.size() != 3){
            while(temp5.size() != 3){
                temp5 += str;
            }
        }else{
            answer = temp5;
        }
    }
    return temp5;
}
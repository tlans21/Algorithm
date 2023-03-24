#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main(){
    string binary[8] = {"000", "001", "010", "011", "100", "101", "110", "111"};
    string num;
    int temp[8];

    cin>>num;
    for (int i = 0; i < num.length(); i++) {

		temp[i] = num[i] - '0';
		if (i == 0){
            cout << stoi(binary[temp[i]]);
        }
		else cout << binary[temp[i]];
	}
}

#include<iostream>
#include<cstring>
#include<map>

using namespace std;

int main(){
    int N;
    cin>>N;
    map<string, int> m1;


    string bomul;
    //hint : 뒤에는 무조건 확장자로 간주
    for(int i = 0; i < N; i++){
        cin>>bomul;
        string answer = bomul.substr(bomul.find('.')+1);
        m1[answer]++;
    }

    for(auto it = m1.begin(); it != m1.end(); it++){
        cout<<(*it).first<<" "<<(*it).second<<'\n';
    }
}
#include<iostream>
#include<map>
#include<string>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string str;
    int kinds = 0;

    map<string, int> m;

    while(getline(cin, str)){
        kinds++;
        m[str]++;
    }
    cout<<fixed;
    cout.precision(4);
    for(auto i = m.begin(); i != m.end(); i++){
        cout<<i->first<<' '<< i->second * 100 / (double)kinds <<'\n';
    }
    return 0;
}
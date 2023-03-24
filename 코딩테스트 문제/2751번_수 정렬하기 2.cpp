#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

bool compare(int first, int last){
    //return frist < last로 작성가능
    if(first < last){
        return true; // true시 오름차순
    }else{
        return false;
    }
}


vector<int> vec;
vector<int>::iterator it; 
int main(){
    //N이 10만이기때문에 nlogn 시간복잡도를 가지는 정렬을 써야한다.
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    
    
    cin>>N;

    for(int i = 0; i < N; i++){
        int num;
        cin>>num;
        vec.push_back(num);
    }

    sort(vec.begin(), vec.end(), compare);

    for(it = vec.begin(); it < vec.end(); it++){
        cout<<*it<<'\n';
    }

    return 0;
}
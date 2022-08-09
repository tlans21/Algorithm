#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int N;
    int M;
    int L;
    cin>>N>>M>>L;
    vector<int> arr;
    arr.push_back(0);
    for(int i = 0; i < N; i++){
        int temp;
        cin>>temp;
        arr.push_back(temp);
    }
    arr.push_back(L);

    sort(arr.begin(), arr.end());

    int left = 1;
    int right = L-1;

    while(left<=right){
        int mid = (left + right) / 2;

        int shelter = 0;
    
        for(int i = 1; i < arr.size(); i++){
            int dist = arr[i]-arr[i-1];
            shelter += (dist / mid);
            if(dist % mid == 0){
                shelter--;
            }
        }

        if(shelter > M){
            left = mid + 1;
        }else{
            right = mid -1;
        }
    }
    cout<<left;
}
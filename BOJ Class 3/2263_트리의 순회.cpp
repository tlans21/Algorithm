#include<iostream>

using namespace std;
int inorder[100001];
int postorder[100001];
int index[100001];

void preorder(int inorder_start, int inoredr_end, int post_start, int post_end){
    if(inorder_start > inoredr_end || post_start > post_end){
        return;
    }
    int root = postorder[post_end];
    cout<<root<<' ';
    int inorder_location = index[root]; // 인오더에서 루트의 위치
    int jump = inorder_location - inorder_start;
    //왼쪽
    preorder(inorder_start, inorder_location-1, post_start, post_start + jump-1);
    //오른쪽
    preorder(inorder_location+1, inoredr_end, post_start+jump, post_end-1);
}

int main(){
    int N;
    cin >> N;

    for(int i = 0; i < N; i++){
        cin >> inorder[i];

    }
    for(int i = 0; i < N; i++){
        cin>>postorder[i];
    }
    for(int i = 0; i < N; i++){
        index[inorder[i]] = i;
    }
    preorder(0, N-1, 0, N-1);
    return 0;
}
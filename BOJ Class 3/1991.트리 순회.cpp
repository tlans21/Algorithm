#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int N;
char X;
char Y;
char Z;
int parent[27][2];

void preorder(char root){
    if(root =='.'){
        return;
    }else{
        cout<<root;
        preorder(parent[root-'A'][0]);
        preorder(parent[root-'A'][1]);
    }
}
void inorder(char root){
    if(root == '.'){
        return;
    }else{
        inorder(parent[root - 'A'][0]);
        cout << root;
        inorder(parent[root - 'A'][1]);
    }
}

void postorder(char root){
    if (root == '.'){
        return;
    }else{
        postorder(parent[root - 'A'][0]);
        postorder(parent[root - 'A'][1]);
        cout << root;
    }
}

int main(){
    cin>> N;
    for(int i = 1; i <= N; i++){
         cin >> X >> Y >> Z;
        parent[X - 'A'][0] = Y;
        parent[X - 'A'][1] = Z;
    }
    preorder('A');
    cout<<'\n';
    inorder('A');
    cout<<'\n';
    postorder('A');
    cout<<'\n';

    return 0;
}
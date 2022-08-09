#include <iostream>

using namespace std;
int number = 15;

// 하나의 노드 정보를 선언합니다.
typedef struct node *treePointer;
typedef struct node {
    string data;
    treePointer leftchild;
    treePointer rightchild;
}node;

//전위 순회

void preorder(treePointer ptr){
    if(ptr){
        cout << ptr->data <<' ';
        preorder(ptr->leftchild);
        preorder(ptr->rightchild);
    }
}

//중위 순회
void inorder(treePointer ptr){
    if(ptr){
        inorder(ptr->leftchild);
        cout << ptr->data <<' ';
        inorder(ptr->rightchild);
    }
}

//후위 순회
void postorder(treePointer ptr){
    if(ptr){
        postorder(ptr->leftchild);
        postorder(ptr->rightchild);
        cout << ptr->data <<' ';
    }
}

int main(void){
    cin >> number;

    node nodes[number + 1];
    for(int i = 1; i <= number; i++){
        nodes[i].data = 'a' + i-1;
        nodes[i].leftchild = NULL;
        nodes[i].rightchild = NULL;
    }

    for(int i = 1; i <= number; i++){
        if(i % 2 == 0){
            nodes[i / 2].leftchild = &nodes[i];
        }else{
            nodes[i / 2].rightchild = &nodes[i];
        }
    }
    preorder(&nodes[1]);
    return 0;
}
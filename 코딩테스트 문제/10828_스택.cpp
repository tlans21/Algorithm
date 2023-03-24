#include<iostream>

using namespace std;

typedef struct Node{
    int data;
    Node *next;
}Node;


typedef struct stack{
    int count;
    Node *top;
}stack;

void Initstack(stack *s){
    s->top = NULL;
    s->count = 0;
}

int empty(stack *s){
    if(s->count == 0){
        return 1;
    }else{
        return 0;
    }
}

void push(stack *s, int num){
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = num;
    newNode->next = s->top;
    s->top = newNode;
    s->count++;
}

int pop(stack *s){
    if(empty(s)){
        return -1;
    }else{
        int value;
        Node *DeleteNode;
        DeleteNode = s->top;
        value = DeleteNode->data;
        s->top = DeleteNode->next;
        free(DeleteNode);
        s->count--; 
        return value;
        
    }
}

int top(stack *s){
    if(empty(s)){
        return -1;
    }else{
        return s->top->data;
    }
}

int size(stack *s){
    return s->count;
}



int main(){
    stack s;
    Initstack(&s);
    int N;
    cin>>N;

    for(int i = 1; i <= N; i++){
        string str;
        cin>>str;
        if(str == "push"){
            int num;
            cin>>num;
            push(&s, num);
        }else if(str == "pop"){
            cout<<pop(&s)<<'\n';
        }else if(str == "size"){
            cout<<size(&s)<<'\n';
        }else if(str == "empty"){
            cout<<empty(&s)<<'\n';
        }else if(str == "top"){
            cout<<top(&s)<<'\n';
        }
    }
    return 0;
}
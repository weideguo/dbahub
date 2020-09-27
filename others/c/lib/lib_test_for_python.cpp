// c++代码要转成c编译才能提供python条用

class TestLib{  
    public:  
        void display();  
        void display(int a);  
};  

void TestLib::display() {  
    cout<<"First display"<<endl;  
}  
  
void TestLib::display(int a) {  
    cout<<"Second display"<<endl;  
}  

extern "C" {  
    TestLib obj;  
    void display() {  
        obj.display();   
    }  
    void display_int() {  
        obj.display(2);   
    }  
}  

#include <stdio.h>   
extern "C" {  
    void display() {  
        printf("This is Display Function\n");   
    }  
} 

//g++ test.cpp -fPIC -shared -o libtest.so

/*
//python中调用

import ctypes  
so = ctypes.CDLL("./libtest.so")  
so.display()  

*/
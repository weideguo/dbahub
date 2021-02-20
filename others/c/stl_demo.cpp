#include <iostream>
#include <vector>
using namespace std;
 
int main()
{   
   
    vector<int> vec; 
    int i;
    
    cout << "vector size = " << vec.size() << endl;
    
    for(i = 0; i < 5; i++){
    vec.push_back(i);
    }
    
    cout << "extended vector size = " << vec.size() << endl;
    
    // 访问向量
    for(i = 0; i < 5; i++){
        cout << "value of vec [" << i << "] = " << vec[i] << endl;
    }
    
    // 使用迭代器 iterator 访问
    vector<int>::iterator v = vec.begin();
    while( v != vec.end()) {
        cout << "value of v = " << *v << endl;
        v++;
    }
    
    // echo $? #获取到的值
    return 0;
}

/*
STL 
标准模板库
提供容器 deque list vector map
*/
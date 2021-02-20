#include <iostream>

#include <thread>

// 在外则获取主线程id，在函数内则获取调用线程的id
std::thread::id main_thread_id = std::this_thread::get_id();

void my_func(int n) {
    std::cout << std::this_thread::get_id() << " start\n";
    std::this_thread::sleep_for(std::chrono::seconds(n));
    std::cout << std::this_thread::get_id() << " pause of " <<  n << " seconds ended\n";
}

int main() {
    //std::thread t(my_func);
    //t.join();
    
    std::thread threads[5];                         
    
    for (int i = 0; i < 5; ++i){
        threads[i] = std::thread(my_func, i + 1);   
    }
    
    for (auto &thread : threads){
        thread.join();
    }
    std::cout << "All done\n";
}
/*
c++ 11 标准库实现线程
g++ -std=c++11 thread_demo_new.cpp -lpthread -o thread_demo_new
*/


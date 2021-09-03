/*
智能
像指针一样使用的值，但提供了自动内存管理的附加功能，当指针不再使用时，它指向的内存被释放
std::unique_ptr   不打算对同一对象持有多个引用时
std::shared_ptr   从多个地方引用对象， 并且不希望在所有这些引用都消失之前释放
std::weak_ptr     从多个地方引用你对象， for those references for which it’s ok to ignore and deallocate (so they’ll just note the object is gone when you try to dereference)

不建议使用以下两种
boost::smart
std::auto_ptr   deprecated in C++11 and removed in C++17
*/


#include <memory>
//使用智能指针需要引用

// 普通指针
MyObject* ptr = new MyObject(); 
ptr->DoSomething(); // Use the object in some way
delete ptr; // Destroy the object. Done with it.
// Wait, what if DoSomething() raises an exception...?


// 智能指针
SomeSmartPtr<MyObject> ptr(new MyObject());
ptr->DoSomething(); // Use the object in some way.

// Destruction of the object happens, depending 
// on the policy the smart pointer class uses.

// Destruction would happen even if DoSomething() 
// raises an exception



void f()
{
    {
       std::unique_ptr<MyObject> ptr(new MyObject());
       ptr->DoSomethingUseful();
    } // ptr goes out of scope -- 
      // the MyObject is automatically destroyed.

    // ptr->Oops(); // Compile error: "ptr" not defined
                    // since it is no longer in scope.
}



void f()
{
    typedef std::shared_ptr<MyObject> MyObjectPtr; // nice short alias
    MyObjectPtr p1; // Empty

    {
        MyObjectPtr p2(new MyObject());
        // There is now one "reference" to the created object
        p1 = p2; // Copy the pointer.
        // There are now two references to the object.
    } // p2 is destroyed, leaving one reference to the object.
    
} // p1 is destroyed, leaving a reference count of zero. 
  // The object is deleted.
  


// 循环依赖时不会被自动释放
struct Owner {
   std::shared_ptr<Owner> other;
};

std::shared_ptr<Owner> p1 (new Owner());
std::shared_ptr<Owner> p2 (new Owner());
p1->other = p2; // p1 references p2
p2->other = p1; // p2 references p1

// Oops, the reference count of of p1 and p2 never goes to zero!
// The objects are never destroyed!


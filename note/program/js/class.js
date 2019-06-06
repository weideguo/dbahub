var P = class {}

class P{
  #x;   //私有属性 只能类内部调用
  constructor(){
    // 关键字 构造函数
    this.x = ''
  }
  f(){}
  // 静态方法 只能通过类直接调用 实例不能调用 可以被继承
  static f1(){}
  // 实例可以直接以属性获取 不能直接调用
  get prop() {
    return 'getter';
  }
  // 实例可以直接以属性设置 不能直接调用
  set prop(value) {...}
  
  * f2(){}
}

// 继承
class PP extends P {
    super()  // 调用父类的构造函数
    super.x  // 调用父类的属性
}

// 向类添加新方法    在此之前或之后所有使用该类初始化的实例都可以调用
Object.assign(P.prototype, {
  ff(){},
  fff(){}
});

// 向类添加新方法 
P.prototype.toString=function(...){...}
// prototyp   为类添加新方法

// __proto__  为类添加新方法 不推荐使用
var o=new P()
o.__proto__.ffff=function(...){...}

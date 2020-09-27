// 实现外部增加函数以及属性

x=function(i){
    this.a=i;}
 
x.prototype.add=function(j){
    this.b=j;
    console.log(this.a+this.b)}

x.prototype.add2=function(k){
    this.c=k;
    console.log(this.b+this.c)}    
    
a=new x()

a.add()
a.add2()

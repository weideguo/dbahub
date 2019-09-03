package kg.tom;
 
public class MyJni {
   
    public native void display();
    public native double sum(double x,double y);
     
    public static void main(String[] args) {

    }
}
/*
javac kg.tom.MyJni.java   #编译成class
javah kg.tom.MyJni        #转成c的头文件，得到头文件kg_tom_MyJni.h
*/

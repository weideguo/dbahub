package kg.tom;
 
public class MyJniTest {
	public native void display();
	public native double sum(double x,double y);
    static {
		System.loadLibrary("sum");
    }       
    public static void main(String[] args) {
		new MyJni().display();
		System.out.println(new MyJni().sum(2.0, 3.0));
    }
}
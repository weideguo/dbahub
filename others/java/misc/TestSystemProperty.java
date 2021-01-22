
public class TestSystemProperty {
	
    public static void main(String agrs[]){
        
        System.out.println(System.getProperty("a.b.c"));
    }
}
        
/*
javac TestSystemProperty.java
java -Da.b.c=aaaa TestSystemProperty
*/        
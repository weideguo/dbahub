
import java.net.URL;


public class ClasspathDemo {
	
    public static void main(String agrs[]){
        // classpath 当前类class文件的URI目录
        URL resource = ClasspathDemo.class.getResource("/");
        //
        URL resource0 = ClassLoader.getSystemResource("");
        // 
        URL resource1 = ClasspathDemo.class.getResource("");
        // 
        URL resource2 = ClasspathDemo.class.getClassLoader().getResource("");
        // null
        URL resource3 = ClasspathDemo.class.getClassLoader().getResource("/");
        
        
        
        System.out.println(resource);
        System.out.println(resource0);
        System.out.println(resource1); 
        System.out.println(resource2);
        System.out.println(resource3);
        

    }
}
              
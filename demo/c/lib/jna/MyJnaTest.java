


//MyJnaTest.java
import com.sun.jna.Library;
import com.sun.jna.Native;
import com.sun.jna.WString;
 

public class MyJnaTest {
 
	public interface TestDll extends Library {
		/**
		* 当前路径是在项目下，而不是bin输出目录下。
		*/
		TestDll INSTANCE = (TestDll1)Native.loadLibrary("TestDll", TestDll.class);
		public void say(WString value);            
	}
	public static void main(String[] args) {
		TestDll.INSTANCE.say(new WString("Hello World!"));
		System.out.println("????");
	}
}
/*
java和c的数据类型映射

boolean								int
byte								char
char								wchar_t
short								short
int									int
long								long long, __int64
float								float
double								double
Buffer Pointer						pointer
<T>[] 								pointer array
String								char*
WString								wchar_t*
String[]							char**
WString[]							wchar_t**
Structure							struct*, struct
Union								union
Structure[]							struct[]
Callback							<T> (*fp)()
NativeMapped						varies
NativeLong							long
PointerType							pointer

*/



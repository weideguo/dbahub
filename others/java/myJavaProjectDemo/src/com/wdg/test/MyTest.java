package com.wdg.test;




// public class MyTest {
//     public static void main(String args[]) {
//         System.out.println("xxxxx");
//     }
// }


import org.apache.log4j.BasicConfigurator;
import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;

import com.wdg.utils.MyUtils;
/*
 * log4j 是日志组件，提供日志记录
 */

public class MyTest {
	
	public static void main(String agrs[]){
		Logger logger=Logger.getLogger(MyTest.class);
		//BasicConfigurator.configure();  //使用默认配置  即没有log4j.properties文件也可以,但不会输出到文件中
		//log4j.appender.DEFAULT_LOG_FILE.File="logs/testlog.log";  //也可使用log4j.properties文件中设置log输出位置
		//PropertyConfigurator.configure("./log4j.properties");  //默认在src目录下 ,执行程序后bin目录如果没有log4j.properties则复制到bin目录，使用的是程序运行使用的是bin目录下的文件
		//使用动态配置
		logger.warn("warn--by wdg");
		logger.info("info--by wdg");
		logger.debug("debug--by wdg");
		logger.error("erroe--by wdg");
        
        MyUtils u = new MyUtils();
        u.output("xxxxxxxx");
        
	}
}
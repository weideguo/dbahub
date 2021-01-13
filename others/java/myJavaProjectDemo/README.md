# 没有任何依赖包简单编译
```shell
#cd src
#javac com/wdg/test/MyTest.java 
#
##运行
#cd src
#java com.wdg.test.MyTest
```

# maven使用
```shell
#由pom.xml文件下载依赖包   下载到 ~/.m2/（缓存，下次运行如果存在则直接从这里获取）并且复制到 ./target/dependency/ 
#mvn -f pom.xml dependency:copy-dependencies     #可以单独制定配置文件
mvn dependency:copy-dependencies

#手动编译与运行
#cd src
#可以编译单个文件 但依赖的文件需要预先编译
#javac -Djava.ext.dirs=../target/dependency/ com/wdg/test/MyTest.java 
#同时编译所有文件
#javac -Djava.ext.dirs=../target/dependency/ com/wdg/test/MyTest.java com/wdg/utils/MyUtils.java 
#运行
#java -Djava.ext.dirs=../target/dependency/ com/wdg/test/MyTest

#默认编译到./target/classes
#mvn -f pom.xml compile
mvn compile

#运行
#cd target/classes
#java -Djava.ext.dirs=../dependency/ com/wdg/test/MyTest

#将./target/classes打包成jar
mvn package

#运行
#cd target
#java -Djava.ext.dirs=./dependency/ -jar javatest-1.0-SNAPSHOT.jar
```

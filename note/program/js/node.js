node.js
实现js在服务端运行



脚本模式
node helloworld.js


交互模式
node //进入命令行


##########################################################################包管理
npm 
node package manage        

npm run run_tag            #run_tag为package.json中scripts块指定的名字
npm run build              #即实际执行 node build/build.js    生成dist目录即可当成静态html项目使用 但不能直接用浏览器打开文件
npm install                #安装所有依赖包
npm install package-name   #安装模块

#####################################################################
npm set registry https://registry.some_other_else       #增加镜像源
npm config rm registry                                  #删除镜像源
npm config list            #npm配置查看

#使用nrm进行源管理
npm install nrm -g --save
nrm ls
nrm use cnpm
nrm current
nrm del cnpm
nrm add cnpm http://r.cnpmjs.org/

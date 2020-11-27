////////////////////////////////////////////////webSQL//////////////////////////////////////////////////////
//w3c标准已经废弃 chrome的使用样例  不同页面通过创建相同名字库查看数据 数据持久保存
let myBase = window.openDatabase("fristBase.db","1.0",null,20000);

//创建表 
myBase.transaction(function(tr){
	tr.executeSql("create table goods(_id Integer primary key autoincrement,name text,price real)")
})

//增加
myBase.transaction(function(tr){
	tr.executeSql("insert into goods(name,price) values(?,?)",["aaa",100])
})

//修改
myBase.transaction(function(tr){
	tr.executeSql("update goods set name = ? , price = ? where _id = ?",["bbb",200,1]);
}) 

//删除
myBase.transaction(function(tr){
	tr.executeSql("delete * from goods where _id = ?",[1])
})

findGoods(){
	let findGood =()=>new Promise(resolve=>{
        myBase.transaction(function(tr){
            //参数：sql语句，参数，成功回调，失败回调
            tr.executeSql("select * from goods",[],
                function(tr,result){
                    resolve(result.rows);
                },
                function(error){
                    alert(error);
                });
            })
		})
		
	//异步查询
	findGood().then(
		value=>{
			// self.GoodsList=value;
			console.log(value);
		})		
	}

findGoods()


////////////////////////////////////////////////webSQL//////////////////////////////////////////////////////




//indexDB
//持久保存 同源共享

/*
//以下操作相同
request.addEventListener('success', e=>{})
request.onsuccess = (e)=>{}
request.onsuccess = function(e){}
*/

/*
upgradeneeded   open时升版本触发
success         open时相同版本触发
*/
// request0.readyState 查看状态

let request0 = indexedDB.open('myDatabase',1);
//只能通过upgradeneeded对数据库结构进行更改 
//因此更改结构需要在open时升级版本 之后的数据操作open时都需要使用新版本
request0.addEventListener('upgradeneeded', e => {
    let db = e.target.result;
    if (!db.objectStoreNames.contains('Users')) {
        let store = db.createObjectStore('Users', {
            keyPath: 'userId',
            autoIncrement: false
        });
        console.log('创建对象仓库成功'); 
    }else{
        console.log('无需再创建对象仓库'); 
    }
});
request0.addEventListener('success', e => {
    console.log('创建对象仓库成功...');
});
request0.addEventListener('error', e => {
    console.log('创建对象仓库失败');
});


//open版本与当前版本一致，触发 success 操作
let request1 = indexedDB.open('myDatabase',1);
request1.addEventListener('success', e => {
    let db = e.target.result;
    let tx = db.transaction('Users', 'readwrite');
    let store = tx.objectStore('Users');
    let reqAdd = store.add({
        'userId': 1,
        'userName': '张三',
        'age': 24
    });
    reqAdd.addEventListener('success', e => {
        console.log('保存成功')
    })
});

//每次操作前都要连接一次 连接才触发操作
let request2 = indexedDB.open('myDatabase',1);
request2.addEventListener('success', e => {
    let db = e.target.result;
    let tx = db.transaction('Users', 'readwrite');
    let store = tx.objectStore('Users');
    let reqGet = store.get(1);
    reqGet.addEventListener('success', e => {
        console.log(e.srcElement.result);
    })
});




//升级版本实现更新表结构  需要先重新刷新页面？
let request00 = indexedDB.open('myDatabase',2);
request00.addEventListener('upgradeneeded', e => {
    let db = e.target.result;
    if (!db.objectStoreNames.contains('Users1')) {
        let store = db.createObjectStore('Users1', {
            keyPath: 'userId',
            autoIncrement: false
        });
        
    }else{
        console.log('更改创建对象仓库成功'); 
    }
});
request00.addEventListener('success', e => {
    console.log('更改对象仓库成功...');
});
request00.addEventListener('error', e => {
    console.log('更改对象仓库失败');
});


//升级版本实现更新表结构  需要先重新刷新页面？
let request01 = indexedDB.open('myDatabase',3);
request01.addEventListener('upgradeneeded', e => {
    let db = e.target.result;
    if (!db.objectStoreNames.contains('Users')) {
        console.log('需要预先创建对象仓库'); 
    }else{
        let txn = e.target.transaction
        let store = txn.objectStore('Users')
        store.createIndex("name_index", "name", { unique: false })
        console.log('更改对象仓库成功')
    } 
});
request01.addEventListener('success', e => {
    console.log('更改对象仓库成功...');
});
request01.addEventListener('error', e => {
    console.log('更改对象仓库失败');
});

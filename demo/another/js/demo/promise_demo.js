异步顺序控制

var promise = new Promise(function(resolve, reject){
    // ... some code
    value=xxx
    error=yyy
    if (/* 操作成功 */) {
        resolve(value);
    } else {
        reject(error);
    }
})


//  demo1
function multiply(input) {
    return new Promise(function (resolve, reject) {
        console.log('calculating ' + input + ' x ' + input + '...');
        setTimeout(resolve, 2000, input * input);
    });
}

function add(input) {
    return new Promise(function (resolve, reject) {
        console.log('calculating ' + input + ' + ' + input + '...');
        setTimeout(resolve, 2000, input + input);
    });
}

var p = new Promise(function (resolve, reject) {
    console.log('start new Promise...');
    resolve(123);
});

p.then(multiply)
 .then(add)
 .then(multiply)
 .then(add)
 .then(function (result) {
    console.log('Got value: ' + result);
});



// demo2
function sleep(ms) {
    return new Promise(function(resolve, reject) {
        setTimeout(resolve, ms);
    })
}
sleep(500).then( ()=> console.log("finished"));


// demo3
let promise = new Promise(function(resolve, reject){
    console.log("AAA");
    resolve()
});
promise.then(() => console.log("BBB"));
console.log("CCC")


